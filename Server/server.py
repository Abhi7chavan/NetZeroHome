from fastapi import FastAPI ,Request
import uvicorn 
import time
from package.logger import logger
from starlette.responses import JSONResponse
from handlers.user_handler import user_router
from handlers.license_handler import license_router
app = FastAPI()

async def logging_middleware(request: Request, call_next):
    """Middleware to log request processing errors."""
    start_time = time.time()
    
    try:
        response = await call_next(request) 
        duration = time.time() - start_time
        logger.info(f"{request.method} {request.url} - {response.status_code} - {duration:.2f}s")
        return response
    except Exception as e:
        duration = time.time() - start_time
        logger.error(
            f"ERROR: {request.method} {request.url} - {str(e)} - Duration: {duration:.2f}s",
            exc_info=True
        )
        raise e  # Pass to exception handler
    


async def global_exception_handler(request: Request, exc: Exception):
    """Global error handler to log minimal exceptions."""
    error_message = f"UNHANDLED ERROR at {request.method} {request.url}: {str(exc)}"
    
    # Log only the basic error message
    logger.error(error_message)  
    
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error. Please try again later."}
    )


#routes
app.include_router(user_router)
app.include_router(license_router)

#attach middleware
app.middleware("http")(logging_middleware)
app.add_exception_handler(Exception,global_exception_handler)





