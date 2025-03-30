from loadModels.load_mbart import load_mbart

def load_model_by_name(model_name):
    match model_name:
        case "mbart":
            return load_mbart()
        # Add more cases here as needed
        case _:
            raise ValueError(f"Model {model_name} is not supported.")
