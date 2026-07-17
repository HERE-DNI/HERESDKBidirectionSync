---
title: "LineDataSource.LineDataProcessor (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-linedatasource-linedataprocessor"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-com-here-sdk-mapview-datasource-package-summary">com.here.sdk.mapview.datasource</a>

</div>

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

Enclosing class:  
<a href="sdk-for-android-explore-com-here-sdk-mapview-datasource-linedatasource" title="class in com.here.sdk.mapview.datasource">LineDataSource</a>

<!-- -->

Functional Interface:  
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

<div class="type-signature">

<span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" class="external-link" title="class or interface in java.lang">@FunctionalInterface</a> </span><span class="modifiers">public static interface </span><span class="element-name type-name-label">LineDataSource.LineDataProcessor</span>

</div>

<div class="block">

Called for each line, allowing inspection, removal or update of coordinates and attributes.

</div>

</div>

- <div id="sdk-for-android-explore-method-summary" class="section method-summary">

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

      process ( LineDataAccessor lineAccessor)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called for each line, allowing inspection, removal or update of coordinates and attributes.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-process-com-here-sdk-mapview-datasource-LineDataAccessor" class="section detail">

    ### process

    <div class="member-signature">

    <span class="return-type">boolean</span> <span class="element-name">process</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-explore-com-here-sdk-mapview-datasource-linedataaccessor" title="class in com.here.sdk.mapview.datasource">LineDataAccessor</a> lineAccessor)</span>

    </div>

    <div class="block">

    Called for each line, allowing inspection, removal or update of coordinates and attributes.

    </div>

    Parameters:  
    `lineAccessor` -

    the line data accessor.

    Returns:  
    value indicating the result of the processing.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

