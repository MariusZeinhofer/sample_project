"""A sample file that prints sample."""


def sample_function(k: int = 2):
    """Compute the batched Hessian of the model w.r.t. its input.

    Args:
        model: The model whose Hessian will be computed. Must produce batched scalars as
            output.
        X: The input to the model. First dimension is the batch dimension.
            Must be differentiab .
            le.

    Returns:
        The Hessians of the model w.r.t. X. Has shape
        `[batch_size, *X.shape[1:], *X.shape[1:]]`.
    """
    print("Just output from a sample function.")


print("Hi there, I am mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm just a sample.")

x = 2 *3 - 4
