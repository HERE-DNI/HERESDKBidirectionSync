---
title: "PolygonDataSource.PolygonDataProcessor (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-polygondatasource-polygondataprocessor"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview.datasource](sdk-for-android-explore-com-here-sdk-mapview-datasource-package-summary)

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

Enclosing class:  
[PolygonDataSource](sdk-for-android-explore-com-here-sdk-mapview-datasource-polygondatasource "class in com.here.sdk.mapview.datasource")

<!-- -->

Functional Interface:  
This is a functional interface and can therefore be used as the
assignment target for a lambda expression or method reference.

<div class="type-signature">

<span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" class="external-link" title="class or interface in java.lang">@FunctionalInterface</a>
</span><span class="modifiers">public static interface
</span><span class="element-name type-name-label">PolygonDataSource.PolygonDataProcessor</span>

</div>

<div class="block">

Called for each polygon, allowing inspection, removal or update of
coordinates and attributes.

</div>

</div>

<div class="section summary">
<div id="sdk-for-android-explore-method-summary"
  class="section method-summary">

  <div id="sdk-for-android-explore-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      process(PolygonDataAccessor polygonAccessor)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called for each polygon, allowing inspection, removal or update of
  coordinates and attributes.

  </div>

  </div>

  </div>

  </div>

  </div>

</div>

<div class="section details">
<div id="sdk-for-android-explore-method-detail"
  class="section method-details">
<div id="sdk-for-android-explore-process(com.here.sdk.mapview.datasource.PolygonDataAccessor)"
    class="section detail">

    ### process

    <div class="member-signature">

    <span class="return-type">boolean</span> <span class="element-name">process</span><span class="parameters">(@NonNull
    [PolygonDataAccessor](sdk-for-android-explore-com-here-sdk-mapview-datasource-polygondataaccessor "class in com.here.sdk.mapview.datasource") polygonAccessor)</span>

    </div>

    <div class="block">

    Called for each polygon, allowing inspection, removal or update of
    coordinates and attributes.

    </div>

    Parameters:  
    `polygonAccessor` -

    the polygon data accessor.

    Returns:  
    value indicating the result of the processing.

    </div>

  </div>

</div>

