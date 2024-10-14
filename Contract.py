{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMOvneXCyEJnJzqupw0Vtl/",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Jax0303/-W3GS-sample/blob/main/Contract.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "YtZO9I0XqDOy"
      },
      "outputs": [],
      "source": [
        "from fastapi import FastAPI\n",
        "from pydantic import BaseModel\n",
        "from typing import List\n",
        "\n",
        "app = FastAPI()\n",
        "\n",
        "# 계약서의 기본 구조를 정의하는 모델\n",
        "class Contract(BaseModel):\n",
        "    최대_방송_길이: int\n",
        "    금지_키워드: List[str]\n",
        "    스포일러_금지: bool\n",
        "    수익화_허용: bool\n",
        "\n",
        "# 하드코딩된 계약 조건 (예시로 스포일러 금지, 수익화 금지 등)\n",
        "계약서 = Contract(\n",
        "    최대_방송_길이=180,  # 최대 3시간 방송 허용\n",
        "    금지_키워드=[\"폭력\", \"음란\", \"스포일러\"],  # 금지된 키워드 목록\n",
        "    스포일러_금지=True,  # 스포일러 금지 여부\n",
        "    수익화_허용=False  # 수익화 허용 여부\n",
        ")\n",
        "\n",
        "# 스포일러 검사를 위한 함수 (간단히 키워드 기반으로)\n",
        "def check_text_for_keywords(text: str, keywords: List[str]) -> bool:\n",
        "    for keyword in keywords:\n",
        "        if keyword in text:\n",
        "            return True\n",
        "    return False\n",
        "\n",
        "# 방송 메타데이터 추출 (모의 함수 - 실제로는 플랫폼 API에서 데이터를 받아와야 함)\n",
        "def extract_metadata(방송플랫폼: str, 방송ID: str):\n",
        "    return {\n",
        "        \"방송ID\": 방송ID,\n",
        "        \"방송플랫폼\": 방송플랫폼,\n",
        "        \"방송제목\": \"영화 결말 포함 방송\",  # 예시 제목\n",
        "        \"영상길이\": 120  # 예: 2시간 방송\n",
        "    }\n",
        "\n",
        "# 방송 내용 분석 (모의 함수 - 실제로는 AI나 자연어 처리를 통해 분석)\n",
        "def analyze_broadcast_content(방송플랫폼: str, 방송ID: str):\n",
        "    return \"이 방송에서는 영화 결말을 이야기합니다.\"  # 예시 방송 내용\n",
        "\n",
        "# API: 방송 검사\n",
        "@app.post(\"/check_broadcast\")\n",
        "def 전자계약_검사(방송ID: str, 방송플랫폼: str):\n",
        "    # 1. 방송 메타데이터 추출\n",
        "    메타정보 = extract_metadata(방송플랫폼, 방송ID)\n",
        "\n",
        "    # 메타데이터 조건 검사\n",
        "    if 메타정보[\"영상길이\"] > 계약서.최대_방송_길이:\n",
        "        return {\"결과\": \"위반: 허용된 방송 길이를 초과함.\"}\n",
        "\n",
        "    if check_text_for_keywords(메타정보[\"방송제목\"], 계약서.금지_키워드):\n",
        "        return {\"결과\": \"위반: 금지된 키워드가 제목에 포함됨.\"}\n",
        "\n",
        "    # 2. 방송 내용 분석\n",
        "    방송내용 = analyze_broadcast_content(방송플랫폼, 방송ID)\n",
        "\n",
        "    # 3. 스포일러 금지 조건 검사\n",
        "    if 계약서.스포일러_금지:\n",
        "        스포일러_여부 = check_text_for_keywords(방송내용, [\"스포일러\", \"결말\", \"Spoiler\"])\n",
        "        if 스포일러_여부:\n",
        "            return {\"결과\": \"위반: 스포일러 송출 금지 위반.\"}\n",
        "\n",
        "    # 위반 사항이 없을 경우\n",
        "    return {\"결과\": \"위반 사항 없음.\"}\n"
      ]
    }
  ]
}