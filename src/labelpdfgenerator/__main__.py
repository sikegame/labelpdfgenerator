from __future__ import annotations

from labelpdfgenerator.label_generator import create_label_pdf
from labelpdfgenerator.models import LabelItem

# mock_data = [
#     {
#         "plantedAt": "2022-06-22",
#         "tagId": "e850b294-95ad-4e3d-9cfd-14f6a22fe015",
#         "strain": {"id": "139O1948", "name": "Nara Haze"},
#     },
#     {
#         "plantedAt": "2022-06-22",
#         "tagId": "5d277c0f-d4d5-4151-90b8-8788fcec1fa3",
#         "strain": {"id": "139O1948", "name": "Nara Haze"},
#     },
#     {
#         "plantedAt": "2022-06-22",
#         "tagId": "f7b25661-c625-4b11-8223-fb5c270564cd",
#         "strain": {"id": "139O1948", "name": "Nara Haze"},
#     },
#     {
#         "plantedAt": "2022-06-22",
#         "tagId": "2370625e-4155-49b3-81f3-17bfd4b15899",
#         "strain": {"id": "139O1948", "name": "Nara Haze"},
#     },
#     {
#         "plantedAt": "2022-06-22",
#         "tagId": "508b8f90-37ef-4f26-a15b-7a3450d7cf5d",
#         "strain": {"id": "139O1948", "name": "Nara Haze"},
#     },
# ]

# items = [
#     LabelItem(
#         qrcode=f"cannakub://plant/{data['tagId']}",
#         lines=[data["strain"]["name"], data["plantedAt"]],
#     )
#     for data in mock_data
# ]


if __name__ == "__main__":
    pdf = create_label_pdf(items)
    with open("test.pdf", 'wb') as f:
        f.write(pdf)
