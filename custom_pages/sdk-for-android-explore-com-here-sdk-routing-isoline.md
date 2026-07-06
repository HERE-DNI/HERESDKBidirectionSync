---
title: "Isoline (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-isoline"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.NativeBasecom.here.sdk.routing.Isoline →
com.here.NativeBase → com.here.sdk.routing.Isoline

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">Isoline</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Represents an isoline polygon around a center point. Any possible route
between the center and any point on the edges of the polygon can be
travelled within the given range restriction. The edges of the polygon
are not guaranteed to be on the road as all reachable road endpoints are
smoothened to fit into one polygon shape. This process can be influenced
by setting IsolineOptions.Calculation.maxPoints .

</div>

</div>

<div class="section summary">

- <div id="sdk-for-android-explore-constructor-summary"
  class="section constructor-summary">

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

      Isoline(IsolineRangeType rangeType,
       double rangeValue,
       MapMatchedCoordinates center,
       List<GeoPolygon> polygons)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Constructs an isoline instance.

  </div>

  </div>

  </div>

  </div>

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`MapMatchedCoordinates`](sdk-for-android-explore-com-here-sdk-routing-mapmatchedcoordinates "class in com.here.sdk.routing")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getCenter()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the center point that was used to calculate this isoline.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a>`<`[`GeoPolygon`](sdk-for-android-explore-com-here-sdk-core-geopolygon "class in com.here.sdk.core")`>`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getPolygons()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets a list of polygons that belong to this isoline.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`IsolineRangeType`](sdk-for-android-explore-com-here-sdk-routing-isolinerangetype "enum class in com.here.sdk.routing")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getRangeType()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the type of the restriction that was used to calculate this
  isoline.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `double`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getRangeValue()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the numerical value of the restriction that was used to calculate
  this isoline.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
  class="external-link"
  title="class or interface in java.lang"><code>equals</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
  class="external-link"
  title="class or interface in java.lang"><code>hashCode</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">

- <div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">

  - <div id="sdk-for-android-explore-<init>(com.here.sdk.routing.IsolineRangeType,double,com.here.sdk.routing.MapMatchedCoordinates,java.util.List)"
    class="section detail">

    ### Isoline

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Isoline</span><span class="parameters">(@NonNull
    [IsolineRangeType](sdk-for-android-explore-com-here-sdk-routing-isolinerangetype "enum class in com.here.sdk.routing") rangeType,
    double rangeValue, @NonNull
    [MapMatchedCoordinates](sdk-for-android-explore-com-here-sdk-routing-mapmatchedcoordinates "class in com.here.sdk.routing") center,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[GeoPolygon](sdk-for-android-explore-com-here-sdk-core-geopolygon "class in com.here.sdk.core")> polygons)</span>

    </div>

    <div class="block">

    Constructs an isoline instance. This instance is provided by the
    CalculateIsolineCallback .

    </div>

    Parameters:  
    `rangeType` -

    Specifies the range type of the provided `rangeValue` list.

    `rangeValue` -

    A list of range values. At least one value must be set.

    `center` -

    The center of the isoline.

    `polygons` -

    A list of polygons that belong to this isoline. At least one value
    must be set.

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-getRangeType()"
    class="section detail">

    ### getRangeType

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[IsolineRangeType](sdk-for-android-explore-com-here-sdk-routing-isolinerangetype "enum class in com.here.sdk.routing")</span> <span class="element-name">getRangeType</span>()

    </div>

    <div class="block">

    Gets the type of the restriction that was used to calculate this
    isoline.

    </div>

    Returns:  
    Specifies the type of the restriction that was used to calculate
    this isoline.

    </div>

  - <div id="sdk-for-android-explore-getRangeValue()"
    class="section detail">

    ### getRangeValue

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getRangeValue</span>()

    </div>

    <div class="block">

    Gets the numerical value of the restriction that was used to
    calculate this isoline.

    </div>

    Returns:  
    Specifies the numerical value of the restriction that was used to
    calculate this isoline.

    </div>

  - <div id="sdk-for-android-explore-getCenter()"
    class="section detail">

    ### getCenter

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapMatchedCoordinates](sdk-for-android-explore-com-here-sdk-routing-mapmatchedcoordinates "class in com.here.sdk.routing")</span> <span class="element-name">getCenter</span>()

    </div>

    <div class="block">

    Gets the center point that was used to calculate this isoline.
    Specifies the center point that was used to calculate this isoline.
    This includes the original center that was passed to the
    RoutingEngine.

    </div>

    Returns:  
    The center point that was used to calculate this isoline.

    </div>

  - <div id="sdk-for-android-explore-getPolygons()"
    class="section detail">

    ### getPolygons

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[GeoPolygon](sdk-for-android-explore-com-here-sdk-core-geopolygon "class in com.here.sdk.core")></span> <span class="element-name">getPolygons</span>()

    </div>

    <div class="block">

    Gets a list of polygons that belong to this isoline. An isoline can
    consist of multiple polygons. For example, islands that can be
    reached by a ferry are included. Each island is then represented as
    a separate polygon. However, in most cases only a single polygon is
    included.

    </div>

    Returns:  
    A list of polygons that belong to this isoline. An isoline can
    consist of multiple polygons. For example, islands that can be
    reached by a ferry are included. Each island is then represented as
    a separate polygon. However, in most cases only a single polygon is
    included.

    </div>

  </div>

</div>

