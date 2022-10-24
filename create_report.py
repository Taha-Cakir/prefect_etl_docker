import datapane as dp
from prefect import flow, task
from prefect_shell import shell_run_command
from prefect.blocks.system import Secret
API_TOKEN="7f2999b3922e3fcd5f84a0f5b6768ecbe10890c0"
@task
def get_dp_token():
    API_TOKEN = "7f2999b3922e3fcd5f84a0f5b6768ecbe10890c0"

    # Access the stored secret
    return API_TOKEN


@flow
def login_into_datapane():
    token = API_TOKEN
    return shell_run_command(f"datapane login --token {token}")


@task
def upload_report(report_elements: list, keyword: str):
    dp.Report(*report_elements).upload(
        name=f"{keyword.title()} Report", publicly_visible=True
    )


@flow(name="Create a Report")
def create_report(report_elements: list, keyword: str):
    login_into_datapane()
    upload_report(report_elements, keyword)