---
title: "PointDataSource.PointDataProcessor (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-datasource-pointdatasource-pointdataprocessor"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-package-summary">com.here.sdk.mapview.datasource</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

Enclosing class:  
<a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-pointdatasource" title="class in com.here.sdk.mapview.datasource">PointDataSource</a>

<!-- -->

Functional Interface:  
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

<div class="type-signature">

<span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" class="external-link" title="class or interface in java.lang">@FunctionalInterface</a> </span><span class="modifiers">public static interface </span><span class="element-name type-name-label">PointDataSource.PointDataProcessor</span>

</div>

<div class="block">

Called for each point, allowing inspection, removal or update of coordinates and attributes.

</div>

</div>

- <div id="sdk-for-android-navigate-method-summary" class="section method-summary">

  <div id="sdk-for-android-navigate-method-summary-table">

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

      process ( PointDataAccessor pointAccessor)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called for each point, allowing inspection, removal or update of coordinates and attributes.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-process-com-here-sdk-mapview-datasource-PointDataAccessor" class="section detail">

    ### process

    <div class="member-signature">

    <span class="return-type">boolean</span> <span class="element-name">process</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-pointdataaccessor" title="class in com.here.sdk.mapview.datasource">PointDataAccessor</a> pointAccessor)</span>

    </div>

    <div class="block">

    Called for each point, allowing inspection, removal or update of coordinates and attributes.

    </div>

    Parameters:  
    `pointAccessor` -

    the point data accessor.

    Returns:  
    value indicating the result of the processing.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

