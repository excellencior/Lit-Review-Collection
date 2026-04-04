# Backpropagation Derivation

## 1\. Final Layer Setup

For the last layer (L):

$$z_k^{(L)} = \sum_j W_{kj}^{(L)} a_j^{(L-1)} + b_k^{(L)}$$

$$a_k^{(L)} = \sigma(z_k^{(L)})$$

Cost: $ C_0 = C(a^{(L)}, y)$

* * *

## 2\. Define the Error Term

$$\delta_k^{(l)} := \frac{\partial C_0}{\partial z_k^{(l)}}$$

* * *

Start from definition:

$$\delta_k^{(L)} = \frac{\partial C_0}{\partial z_k^{(L)}}$$

Apply chain rule:

$$\delta_k^{(L)} = \frac{\partial C_0}{\partial a_k^{(L)}} \cdot \frac{\partial a_k^{(L)}}{\partial z_k^{(L)}}$$

Since:

$$a_k^{(L)} = \sigma(z_k^{(L)})$$

We get:

$$\delta_k^{(L)} = \frac{\partial C_0}{\partial a_k^{(L)}} \cdot \sigma'(z_k^{(L)})$$

* * *

We compute:

$$\delta_j^{(L-1)} = \frac{\partial C_0}{\partial z_j^{(L-1)}}$$

* * *

## 5\. Apply Chain Rule (Key Step)

Since $z_j^{(L-1)}$ affects all $z_k^{(L)}$:

$$\delta_j^{(L-1)} = \sum_k \frac{\partial C_0}{\partial z_k^{(L)}} \cdot \frac{\partial z_k^{(L)}}{\partial z_j^{(L-1)}}$$

Substitute:

$ \frac{\partial C_0}{\partial z_k^{(L)}} = \delta_k^{(L)}$

So:

$$\delta_j^{(L-1)} = \sum_k \delta_k^{(L)} \cdot \frac{\partial z_k^{(L)}}{\partial z_j^{(L-1)}}$$

* * *

## 6\. Compute the Derivative Term

From:

$$z_k^{(L)} = \sum_j W_{kj}^{(L)} a_j^{(L-1)} + b_k^{(L)}$$

We get:

$$\frac{\partial z_k^{(L)}}{\partial a_j^{(L-1)}} = W_{kj}^{(L)}$$

And:

$$\frac{\partial a_j^{(L-1)}}{\partial z_j^{(L-1)}} = \sigma'(z_j^{(L-1)})$$

* * *

## 7\. Chain Them

$$\frac{\partial z_k^{(L)}}{\partial z_j^{(L-1)}} =
W_{kj}^{(L)} \cdot \sigma'(z_j^{(L-1)})$$

* * *

## 8\. Substitute Back

$$\delta_j^{(L-1)} = \sum_k \delta_k^{(L)} \cdot W_{kj}^{(L)} \cdot \sigma'(z_j^{(L-1)})$$

Factor:

$$\delta_j^{(L-1)} =
\left(\sum_k \delta_k^{(L)} W_{kj}^{(L)}\right)
\cdot \sigma'(z_j^{(L-1)})$$

* * *

## 9\. General Back-prop Formula

$$\delta_j^{(l)} =
\left(\sum_k \delta_k^{(l+1)} W_{kj}^{(l+1)}\right)
\cdot \sigma'(z_j^{(l)})$$

* * *

## 10\. Gradients of Parameters

### Weights

From:

$$z_i^{(l)} = \sum_j W_{ij}^{(l)} a_j^{(l-1)} + b_i^{(l)}$$

$$\frac{\partial C_0}{\partial W_{ij}^{(l)}}
= \delta_i^{(l)} \cdot a_j^{(l-1)}$$

* * *

### Bias

$\frac{\partial C_0}{\partial b_i^{(l)}} = \delta_i^{(l)} $

* * *

## Final Clean Summary

$$\delta_k^{(L)} =
\frac{\partial C_0}{\partial a_k^{(L)}} \cdot \sigma'(z_k^{(L)})$$

$$\delta_j^{(l)} =
\left(\sum_k \delta_k^{(l+1)} W_{kj}^{(l+1)}\right)
\cdot \sigma'(z_j^{(l)})$$

$$\frac{\partial C_0}{\partial W_{ij}^{(l)}} = \delta_i^{(l)} a_j^{(l-1)}, \quad \frac{\partial C_0}{\partial b_i^{(l)}} = \delta_i^{(l)} $$