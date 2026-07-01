---
title: "MapContext.SetMemoryManagementOptionsCallback (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapcontext-setmemorymanagementoptionscallback"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div id="class-description" class="section class-description">

Enclosing class:  
[MapContext](sdk-for-android-explore-com-here-sdk-mapview-mapcontext "class in com.here.sdk.mapview")

<!-- -->

Functional Interface:  
This is a functional interface and can therefore be used as the
assignment target for a lambda expression or method reference.

<div class="type-signature">

<span class="annotations"><a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html"
class="external-link"
title="class or interface in java.lang">@FunctionalInterface</a>
</span><span class="modifiers">public static interface
</span><span class="element-name type-name-label">MapContext.SetMemoryManagementOptionsCallback</span>

</div>

<div class="block">

Callback to handle the memory management result. Note: This is a beta
release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation
process.

</div>

</div>

<div class="section summary">

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Instance Methods
  Abstract Methods

  </div>

  <div id="method-summary-table.tabpanel"
  aria-labelledby="method-summary-table-tab0" role="tabpanel">

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Method</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>onSetMemoryManagementOptions(MapContext.MemoryManagementResult result)</code></pre></td>
  <td><div class="block">
  Callback to handle the memory management result.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

</div>

<div class="section details">

- <div id="method-detail" class="section method-details">

  - <div id="onSetMemoryManagementOptions(com.here.sdk.mapview.MapContext.MemoryManagementResult)"
    class="section detail">

    ### onSetMemoryManagementOptions

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onSetMemoryManagementOptions</span><span class="parameters">(@NonNull
    [MapContext.MemoryManagementResult](sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementresult "class in com.here.sdk.mapview") result)</span>

    </div>

    <div class="block">

    Callback to handle the memory management result. Note: This is a
    beta release of this feature, so there could be a few bugs and
    unexpected behavior. Related APIs may change for new releases
    without a deprecation process.

    </div>

    Parameters:  
    `result` -

    The memory management result.

    </div>

  </div>

</div>

