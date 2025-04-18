import torch
if torch.cuda.is_available():
    gpu_count = torch.cuda.device_count()
    print(f"Number of GPUs available: {gpu_count}\n")

    # Iterate through all GPUs
    for i in range(gpu_count):
        props = torch.cuda.get_device_properties(i)
        print(f"GPU {i}: {props.name}")
        print(f"  - Total Memory: {props.total_memory / 1e9:.2f} GB")
        print(f"  - Compute Capability: {props.major}.{props.minor}")
        print(f"  - Multi-Processor Count: {props.multi_processor_count}\n")
else:
    print("No GPUs available.")