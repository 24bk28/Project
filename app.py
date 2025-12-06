import random
import gradio as gr


def generate_list():
    data = sorted(random.sample(range(1, 100), 25))
    print("Generated List:", data)
    return str(data), data


def linear_search_sorted(data, value):
    index = 0
    steps = []

    while index < len(data) and data[index] < value:
        steps.append(f"Checking index {index} with value {data[index]}")
        index += 1

    if index >= len(data) or data[index] != value:
        steps.append("Value not found. Please try another.")
        return -1, steps

    steps.append(f"Checking index {index} with value {data[index]}")
    steps.append(f"Value found at index {index}.")
    return index, steps


def linear_search_on_state(target_str, data_state):
    if not data_state:
        return "Please click Generate List first.", "", ""

    try:
        value = int(target_str)
    except ValueError:
        return "Error: Target must be an integer.", "", str(data_state)

    data = data_state[:]
    position, steps = linear_search_sorted(data, value)

    if position == -1:
        return (
            "Value not found. Please try another.",
            "\n".join(steps),
            str(data),
        )

    return (
        f"Value found at index {position}.",
        "\n".join(steps),
        str(data),
    )


with gr.Blocks(title="Linear Search") as demo:

    gr.HTML(
        """
        <style>
        .gradio-container {
            background-color: #f3f4f6 !important;
            font-family: Arial, sans-serif;
        }

        h1, h2, h3 {
            color: #1f2937 !important;
        }

        p {
            color: #111827 !important;
        }

        button {
            background-color: #60A5FA !important;
            color: black !important;
            border-radius: 8px !important;
            border: none !important;
        }

        button:hover {
            background-color: #FDE68A !important;
        }

        input, textarea {
            border: 2px solid #60A5FA !important;
            border-radius: 6px !important;
        }

        label {
            color: #1f2937 !important;
            font-weight: 600 !important;
        }

        .steps-black textarea {
            background-color: #000000 !important;
            color: #FFFFFF !important;
        }
        </style>
        """
    )

    gr.Markdown(
        """
        # Linear Search Visualizer

        This app generates a sorted list and shows step-by-step linear search.
        """
    )

    data_state = gr.State([])

    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### Controls")
            gen_button = gr.Button("Generate List")
            target_input = gr.Textbox(label="Target value (integer)")
            run_button = gr.Button("Run Linear Search")

        with gr.Column(scale=2):
            gr.Markdown("### Generated List")
            list_output = gr.Textbox(
                interactive=False,
                lines=4,
                label="Current List"
            )

    gr.Markdown("---")

    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### Result")
            result_output = gr.Textbox(
                interactive=False,
                lines=2,
                label="Search Result"
            )

        with gr.Column(scale=2):
            gr.Markdown("### Checks (Step-by-step)")
            steps_output = gr.Textbox(
                interactive=False,
                lines=14,
                label="Search Steps",
                elem_classes=["steps-black"],
            )

    gen_button.click(
        fn=generate_list,
        inputs=[],
        outputs=[list_output, data_state],
    )

    run_button.click(
        fn=linear_search_on_state,
        inputs=[target_input, data_state],
        outputs=[result_output, steps_output, list_output],
    )


if __name__ == "__main__":
    demo.launch()
