---
title: "AvoidCorridorAreaOptions (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-avoidcorridorareaoptions"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-com-here-sdk-routing-package-summary">com.here.sdk.routing</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.routing.AvoidCorridorAreaOptions → com.here.sdk.routing.AvoidCorridorAreaOptions

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">AvoidCorridorAreaOptions</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Area of corridor shape which routes must not cross and exceptions for this area.

</div>

</div>

- <div id="sdk-for-android-explore-field-summary" class="section field-summary">

  <div class="caption">

  Fields

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Field

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-core-geocorridor" title="class in com.here.sdk.core">`GeoCorridor`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-avoidcorridorareaoptions#avoidCorridorArea" class="member-name-link"><code>avoidCorridorArea</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Area of corridor shape which routes must not cross.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-explore-com-here-sdk-core-geobox" title="class in com.here.sdk.core">`GeoBox`</a>`>`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-avoidcorridorareaoptions#boundingBoxExceptionAreas" class="member-name-link"><code>boundingBoxExceptionAreas</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Areas of rectangular shape to exclude from avoidance.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-explore-com-here-sdk-core-geocorridor" title="class in com.here.sdk.core">`GeoCorridor`</a>`>`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-avoidcorridorareaoptions#corridorExceptionAreas" class="member-name-link"><code>corridorExceptionAreas</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Areas of corridor shape to exclude from avoidance.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-explore-com-here-sdk-core-geopolygon" title="class in com.here.sdk.core">`GeoPolygon`</a>`>`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-avoidcorridorareaoptions#polygonExceptionAreas" class="member-name-link"><code>polygonExceptionAreas</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Areas of polygon shape to exclude from avoidance.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-constructor-summary" class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Constructor

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-constructor-name even-row-color">

      AvoidCorridorAreaOptions ( GeoCorridor avoidCorridorArea)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      equals ( Object obj)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      hashCode ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-field-detail" class="section field-details">

  - <div id="sdk-for-android-explore-avoidCorridorArea" class="section detail">

    ### avoidCorridorArea

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-core-geocorridor" title="class in com.here.sdk.core">GeoCorridor</a></span> <span class="element-name">avoidCorridorArea</span>

    </div>

    <div class="block">

    Area of corridor shape which routes must not cross. Strictly enforced. Violations are reported as SectionNoticeCode.VIOLATED_BLOCKED_ROAD . Note: This avoidance option is not supported for IsolineOptions . If it is defined for isoline calculation then an \[sdk.routing.RoutingError.INVALID_PARAMETER\] error is generated. Even though GeoCorridor.half_width_in_meters is an optional property in case of exception areas it is mandatory. Otherwise route calculation will fail with an \[sdk.routing.RoutingError.INVALID_PARAMETER\] error.

    </div>

    </div>

  - <div id="sdk-for-android-explore-boundingBoxExceptionAreas" class="section detail">

    ### boundingBoxExceptionAreas

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-explore-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a>\></span> <span class="element-name">boundingBoxExceptionAreas</span>

    </div>

    <div class="block">

    Areas of rectangular shape to exclude from avoidance.

    </div>

    </div>

  - <div id="sdk-for-android-explore-polygonExceptionAreas" class="section detail">

    ### polygonExceptionAreas

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-explore-com-here-sdk-core-geopolygon" title="class in com.here.sdk.core">GeoPolygon</a>\></span> <span class="element-name">polygonExceptionAreas</span>

    </div>

    <div class="block">

    Areas of polygon shape to exclude from avoidance.

    </div>

    </div>

  - <div id="sdk-for-android-explore-corridorExceptionAreas" class="section detail">

    ### corridorExceptionAreas

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-explore-com-here-sdk-core-geocorridor" title="class in com.here.sdk.core">GeoCorridor</a>\></span> <span class="element-name">corridorExceptionAreas</span>

    </div>

    <div class="block">

    Areas of corridor shape to exclude from avoidance. Note: Even though GeoCorridor.half_width_in_meters is an optional property in case of exception areas it is mandatory. Otherwise route calculation will fail with an \[sdk.routing.RoutingError.INVALID_PARAMETER\] error.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-explore-init-com-here-sdk-core-GeoCorridor" class="section detail">

    ### AvoidCorridorAreaOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">AvoidCorridorAreaOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-explore-com-here-sdk-core-geocorridor" title="class in com.here.sdk.core">GeoCorridor</a> avoidCorridorArea)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `avoidCorridorArea` -

    Area of corridor shape which routes must not cross. Strictly enforced. Violations are reported as <a href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#VIOLATED_BLOCKED_ROAD">`SectionNoticeCode.VIOLATED_BLOCKED_ROAD`</a>. **Note:** This avoidance option is not supported for `IsolineOptions`. If it is defined for isoline calculation then an \[sdk.routing.RoutingError.INVALID_PARAMETER\] error is generated. Even though `GeoCorridor.half_width_in_meters` is an optional property in case of exception areas it is mandatory. Otherwise route calculation will fail with an \[sdk.routing.RoutingError.INVALID_PARAMETER\] error.

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-equals-java-lang-Object" class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr></wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-explore-hashCode" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

