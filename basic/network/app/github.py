import plotly.graph_objects as go
import requests

URL = "https://api.github.com/search/repositories"
QUERY = "?q=language:python+sort:stars+stars:>10000"
HEADERS = {"Accept": "application/vnd.github.v3+json"}
TIMEOUT = 10


def fetch_repositories():
    response = requests.get(f"{URL}{QUERY}", headers=HEADERS, timeout=TIMEOUT)
    print(f"请求状态码：{response.status_code}")
    response.raise_for_status()

    response_dict = response.json()
    print(f"返回项目总数：{response_dict['total_count']}")
    print(f"数据完整：{not response_dict['incomplete_results']}")
    return response_dict["items"]


def build_chart(repo_dicts):
    repo_links, stars, hover_texts = [], [], []

    for repo_dict in repo_dicts:
        repo_name = repo_dict["name"]
        repo_url = repo_dict["html_url"]
        repo_links.append(f"<a href='{repo_url}'>{repo_name}</a>")

        stars.append(repo_dict["stargazers_count"])

        owner = repo_dict["owner"]["login"]
        desc = repo_dict["description"] or "无描述"
        short_desc = desc if len(desc) <= 50 else f"{desc[:50]}..."
        hover_texts.append(f"{owner}<br>{short_desc}")

    fig = go.Figure(
        data=[
            go.Bar(
                x=repo_links,
                y=stars,
                hovertext=hover_texts,
                hovertemplate="%{hovertext}<extra></extra>",
                marker={"color": "SteelBlue", "opacity": 0.7},
            )
        ]
    )
    fig.update_layout(
        title="GitHub上星数最多的Python项目",
        xaxis_title="项目",
        yaxis_title="星数",
        title_font_size=24,
        xaxis_title_font_size=16,
        yaxis_title_font_size=16,
    )
    return fig


def main():
    repo_dicts = fetch_repositories()
    fig = build_chart(repo_dicts)
    fig.show()


if __name__ == "__main__":
    main()
