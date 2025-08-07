# Gram-schmidt-orthogonalisation
In linear algebra, orthogonal bases have many beautiful properties. For example, matrices consisting of orthogonal column vectors (a. k. a. orthogonal matrices) can be easily inverted by just transposing the matrix. Also, it is easier for example to project vectors on subspaces spanned by vectors that are orthogonal to each other. The Gram-Schmidt process is an important algorithm that allows us to convert an arbitrary basis to an orthogonal one spanning the same subspace.
Gram-Schmidt process Permalink

Consider some arbitrary dd-dimensional subspace A=⟨a1,…,an⟩
spanned by linear independent vectors a1,…,ada1​,…,ad​. We want to find the following basis spanning the same subspace: A=⟨q1,…,qd⟩
The Gram-Schmidt process is a typical dynamic programming algorithm, because the core idea behind it is to make ⟨q1,…,qi⟩an orthogonal basis assuming ⟨q1,…,qi−1⟩ is already such a basis. The construction works as follows:

Step 1: For q1q1​, we can just take a1a1​ and normalize it: q1:=a1∥a1∥q1​:=∥a1​∥a1​​

Step 2: q2q2​ must be orthogonal to ⟨q1⟩⟨q1​⟩, so we need to find out the component of a2a2​ that is orthogonal to ⟨q1⟩⟨q1​⟩. We can do this by subtracting the projection of a2a2​ onto ⟨q1⟩⟨q1​⟩ from a2a2​: q2′:=a2−(q1⊤a2)q1q1⊤q1=a2−(q1⊤a2)q1q2′​:=a2​−q1⊤​q1​(q1⊤​a2​)q1​​=a2​−(q1⊤​a2​)q1​

The second equality holds because we normalized the q1q1​ vector and the denominator is thus equal to one.
