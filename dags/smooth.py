from airflow.decorators import dag
from airflow.operators.smooth import SmoothOperator
from datetime import datetime


@dag(
    schedule="@hourly",
    start_date=datetime(2025, 3, 22),
    catchup=False,
    tags=["smooth"],
)
def smooth()
    video = SmoothOperator(
        task_id="youtube_video"
    )


smooth()
