# Contract and proof boundaries

For a positive BF16 group maximum a and magnitude 0 <= x <= a, the scale is
F32 nearest-even RN32(a/6), with gradual underflow. The all-zero fallback is
2^-42. Arbitrary F32 inputs, independently chosen scales, FTZ changes, NaNs,
infinities, other probability-bit budgets and changed RNG policies are outside
the claimed contract. Sign, negative zero, logical random-word addresses,
lazy prefix policy, packing and consumer composition are held fixed.

The canonical observation is the E2M1 interval/base and the integer floor of
the interval probability scaled by 2^32. Saturation and zero are handled
separately. Precision p is an abstract significant-bit precision in 35..64
with binary64 exponent range; it is not a claim of native p45/p49 instructions.

For positive normal derived scales, the p45 proof reduces to 1,600 coefficient/t
branches and 2,814 J/eta branches. Of 236 coarse candidates, 234 violate the
normalized X range and two violate eta. Complete finite checking is part of
the proof. The historical normal review does not independently regenerate
those 236 candidates. A new independent normal checker has not been executed.

For positive subnormal derived scales, p49 sufficiency uses a 4,656-branch
certificate. Its relaxed survivor reconstructs X=531 at u=15 and nonintegral
X at larger u, excluding legal BF16 coefficients. The separate direct-j
implementation ran once with prior exposure disclosed: 124,640 congruence
checks, one survivor and six reconstructions. This is not blind replication,
independent human review or formal proof. The full every-j ledger is omitted.

Normal p45 implies normal p49 by the stated precision monotonicity. Combining
normal and subnormal sufficiency with zero/saturation gives full-domain p49.
The legal p44 and p48 witnesses supply the respective lower bounds within
the declared family. No lower bound for all FP4 algorithms or p<35 is claimed.

The retained scalar bridge concerns specified source arithmetic. It does not
prove CUDA race freedom, compiler correctness, exact executed-cubin identity,
elimination of internal U64 quotient repair, exact real-probability unbiasedness,
random-stream independence or application/model quality.

General double-rounding and stochastic-rounding theory remain relevant.
The exact Rump draft-to-final correspondence and closest-theory derivability
remain UNKNOWN/OPEN. Named-rule mismatch is not whole-framework non-derivability,
and unavailable primary-source bytes are not evidence of originality.
