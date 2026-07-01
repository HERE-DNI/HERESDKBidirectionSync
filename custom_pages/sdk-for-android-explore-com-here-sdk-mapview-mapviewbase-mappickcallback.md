---
title: "MapViewBase.MapPickCallback (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapviewbase-mappickcallback"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div id="class-description" class="section class-description">

Enclosing interface:  
[MapViewBase](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase "interface in com.here.sdk.mapview")

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
</span><span class="element-name type-name-label">MapViewBase.MapPickCallback</span>

</div>

<div class="block">

Callback for a pick request. In case of an error the result is not set.

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
  <td><pre><code>onPickMap(MapPickResult mapPickResult)</code></pre></td>
  <td><div class="block">
  Callback for a pick request.
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

  - <div id="onPickMap(com.here.sdk.mapview.MapPickResult)"
    class="section detail">

    ### onPickMap

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onPickMap</span><span class="parameters">(@Nullable
    [MapPickResult](sdk-for-android-explore-com-here-sdk-mapview-mappickresult "class in com.here.sdk.mapview") mapPickResult)</span>

    </div>

    <div class="block">

    Callback for a pick request. In case of an error the result is not
    set.

    </div>

    Parameters:  
    `mapPickResult` -

    The operation result.

    </div>

  </div>

</div>

