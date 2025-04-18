
# PyTorch Essentials (torch + python)

## Overview

- **Definition**: Open-source deep learning library by **Meta AI (FAIR)**
- **Origin**: Python adaptation of **Lua-based** Torch library, **torch or tesorflow uses static graph**, but **pytorch** uses **Dynamic** computation graph made debuginng and exprimentation become easy.
- **Purpose**: Research and production ML applications


## Core Features

- **Tensors**: NumPy-like arrays with **GPU** acceleration
- **Autograd**: Automatic differentiation for neural networks
- **Dynamic Computation**: On-the-fly graph building for flexibility
- **nn.Module**: Building blocks for neural network architectures
- **GPU Support**: Seamless **CUDA** integration
- **Rich Ecosystem**: Domain-specific libraries (Vision, Text, Audio)


## PyTorch vs TensorFlow

| Aspect | PyTorch | TensorFlow |
| :-- | :-- | :-- |
| Computation | Dynamic (define-by-run) | Static with eager execution |
| User Experience | Pythonic, research-friendly | Production-oriented |
| Debugging | Native Python debugging | More complex tooling |
| Deployment | Improving (TorchScript) | Strong production support |
| Community | Dominates research (~75%) | Strong in industry |
| Best For | Research, prototyping, NLP/CV | Enterprise, large-scale ML |

## Core Modules

- `torch`: Tensor operations with GPU support
- `torch.autograd`: Gradient computation
- `torch.nn`: Neural network components
- `torch.optim`: Optimization algorithms
- `torch.utils`: Data loading utilities
- Domain libraries: `torchvision`, `torchtext`, `torchaudio`


## Key Interview Q\&A

**Q: How to use GPU in PyTorch?**

```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tensor = torch.tensor([1,2,3]).to(device)
```

**Q: Real-world PyTorch applications?**
A: Computer vision, NLP, generative models, reinforcement learning, healthcare AI, autonomous vehicles, and recommendation systems.

**Q: PyTorch vs TensorFlow key differences?**
A: PyTorch uses dynamic graphs (easier debugging, more flexible) while TensorFlow traditionally used static graphs (better production deployment, scalability).

| Feature | PyTorch | TensorFlow |
| :-- | :-- | :-- |
| **Computation Graph** | Dynamic (define-by-run) | Static (define-then-run), now supports eager |
| **Ease of Use** | Pythonic, intuitive, research-friendly | More complex, improving with Keras |
| Debugging | Native Python tools, immediate errors | Requires special tools, more complex |
| **Performance**| Fast for small/medium models | Better for large-scale/distributed models |
| Deployment | Improving, TorchScript, ONNX | Mature, TensorFlow Serving/Lite/JS/TFX |
| **Visualization** | Basic, third-party tools | Advanced (TensorBoard) |
| Community | Dominant in research, growing in industry | Strong in industry, enterprise focus |
| Best For | Research, prototyping, experimentation | Production, enterprise, large-scale ML |

