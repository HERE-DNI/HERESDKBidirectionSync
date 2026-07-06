---
title: "PolylineSimplificationCallback (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-polylinesimplificationcallback"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core](sdk-for-android-explore-com-here-sdk-core-package-summary)

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

Functional Interface:  
This is a functional interface and can therefore be used as the
assignment target for a lambda expression or method reference.

<div class="type-signature">

<span class="annotations"><a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html"
class="external-link"
title="class or interface in java.lang">@FunctionalInterface</a>
</span><span class="modifiers">public interface
</span><span class="element-name type-name-label">PolylineSimplificationCallback</span>

</div>

<div class="block">

The method will be called on the main thread when
PolylineSimplifier.simplify(java.util.List ,
com.here.sdk.core.PolylineSimplifier.Options,
com.here.sdk.core.PolylineSimplificationCallback) is finished.

</div>

</div>

<div class="section summary">

- <div id="sdk-for-android-explore-method-summary"
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

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      onPolylineSimplified(PolylineSimplificationError queryError,
       List<GeoCoordinates> result)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  The method will be called on the main thread when
  PolylineSimplifier.simplify(java.util.List ,
  com.here.sdk.core.PolylineSimplifier.Options,
  com.here.sdk.core.PolylineSimplificationCallback) is finished.

  </div>

  </div>

  </div>

  </div>

  </div>

</div>

<div class="section details">

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-onPolylineSimplified(com.here.sdk.core.PolylineSimplificationError,java.util.List)"
    class="section detail">

    ### onPolylineSimplified

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onPolylineSimplified</span><span class="parameters">(@Nullable
    [PolylineSimplificationError](sdk-for-android-explore-com-here-sdk-core-polylinesimplificationerror "enum class in com.here.sdk.core") queryError,
    @Nullable <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")\> result)</span>

    </div>

    <div class="block">

    The method will be called on the main thread when
    PolylineSimplifier.simplify(java.util.List ,
    com.here.sdk.core.PolylineSimplifier.Options,
    com.here.sdk.core.PolylineSimplificationCallback) is finished.

    </div>

    Parameters:  
    `queryError` -

    The optional error, which occurred during simplification.

    `result` -

    The simplified polyline with number of points less or equal to the
    input polyline of
    [](sdk-for-android-explore-com-here-sdk-core-polylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback))

        PolylineSimplifier.simplify(java.util.List, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)

    .

    </div>

  </div>

</div>

