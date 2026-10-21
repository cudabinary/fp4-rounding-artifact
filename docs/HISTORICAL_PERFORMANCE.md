# Historical performance and limits

The CSV contains all 72 retained H100 NVL summary rows: 24 core rows and 48
generality rows, covering B and the stronger scalar FP64 A-double-prime baseline.
Its `speedup` is baseline time divided by candidate time. Values below one
mean the candidate is slower. All stored digits and intervals are retained.

For the fixed three-layer NVL aggregate, D1/B speedup is
1.0379325903247738 for producer and 1.0319024294254902 for producer plus
consumer. Against A-double-prime the corresponding values are
0.8560589506928495 and 0.8779685570219048. Thus D1 is 16.814385176470847%
longer in producer time than A-double-prime in that NVL aggregate.
These are copied historical estimates, not newly computed results.

Core inputs are the three fixed model-derived layers, N=360000, block256,
producer grid352 and consumer grid1407. Input preparation was CPU regeneration;
it was not recovery of native H100 activations from the measured model forward.
Events enclosed 32 producer operations or 32 two-kernel pairs, with time divided
by32. Transfers, archival operations and CPU wall time were excluded. The
historical protocol used 20 warmups, ten temporal cycles and six balanced
orders. Adjusted intervals describe within-session fixed-cycle uncertainty,
not independent workloads or a new population of model executions.

Historical SXM prose reports 3.15% producer-time reduction over B and 16.45%
longer producer time than A-double-prime. These belong to another device/process
session. They are not reconstructed into an SXM timing table or pooled with
NVL. Producer and two-kernel chain modes are separate; chain timing is not
model end-to-end execution. Synthetic repeated-boundary conditions are not
a natural application workload family. A-double-prime's ordinary/Gaussian
advantage remains part of the conclusion.

Correctness reports cover 105 cases and 37,255,808 values per arm and phase,
before and after timing, over seven fields. Diagnostic entries for base,
threshold and RNG are not a trace of the opaque timed kernel. Exact executed
binary identity and runtime causality remain unverified. The package contains
no new samples, bootstrap run, GPU timing, causal attribution or model-quality test.
