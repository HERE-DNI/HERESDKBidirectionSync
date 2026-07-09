---
title: "MapViewBase.MapPickCallback (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase-mappickcallback"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-mapview-package-summary">com.here.sdk.mapview</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

Enclosing interface:  
<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a>

<!-- -->

Functional Interface:  
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

<div class="type-signature">

<span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" class="external-link" title="class or interface in java.lang">@FunctionalInterface</a> </span><span class="modifiers">public static interface </span><span class="element-name type-name-label">MapViewBase.MapPickCallback</span>

</div>

<div class="block">

Callback for a pick request. In case of an error the result is not set.

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

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      onPickMap ( MapPickResult mapPickResult)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Callback for a pick request.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onPickMap-com-here-sdk-mapview-MapPickResult" class="section detail">

    ### onPickMap

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onPickMap</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-mapview-mappickresult" title="class in com.here.sdk.mapview">MapPickResult</a> mapPickResult)</span>

    </div>

    <div class="block">

    Callback for a pick request. In case of an error the result is not set.

    </div>

    Parameters:  
    `mapPickResult` -

    The operation result.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

