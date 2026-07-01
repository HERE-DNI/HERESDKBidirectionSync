---
title: "PointDataSource.PointDataProcessor (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-pointdatasource-pointdataprocessor"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview.datasource](sdk-for-android-explore-com-here-sdk-mapview-datasource-package-summary)

</div>

<div id="class-description" class="section class-description">

Enclosing class:  
[PointDataSource](sdk-for-android-explore-com-here-sdk-mapview-datasource-pointdatasource "class in com.here.sdk.mapview.datasource")

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
</span><span class="element-name type-name-label">PointDataSource.PointDataProcessor</span>

</div>

<div class="block">

Called for each point, allowing inspection, removal or update of
coordinates and attributes.

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
  <td><code>boolean</code></td>
  <td><pre><code>process(PointDataAccessor pointAccessor)</code></pre></td>
  <td><div class="block">
  Called for each point, allowing inspection, removal or update of
  coordinates and attributes.
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

  - <div id="process(com.here.sdk.mapview.datasource.PointDataAccessor)"
    class="section detail">

    ### process

    <div class="member-signature">

    <span class="return-type">boolean</span> <span class="element-name">process</span><span class="parameters">(@NonNull
    [PointDataAccessor](sdk-for-android-explore-com-here-sdk-mapview-datasource-pointdataaccessor "class in com.here.sdk.mapview.datasource") pointAccessor)</span>

    </div>

    <div class="block">

    Called for each point, allowing inspection, removal or update of
    coordinates and attributes.

    </div>

    Parameters:  
    `pointAccessor` -

    the point data accessor.

    Returns:  
    value indicating the result of the processing.

    </div>

  </div>

</div>

