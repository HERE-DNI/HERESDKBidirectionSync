---
title: "GeoPolygon (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-geopolygon"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core](sdk-for-android-explore-com-here-sdk-core-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.core.GeoPolygon

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">GeoPolygon</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Represents a GeoPolygon area as a series of geographic coordinates, and
optionally, a list of inner boundaries (also known as holes). An
instance of this class, initialized with appropriate vertices.

</div>

</div>

<div class="section summary">

- <div id="sdk-for-android-explore-field-summary"
  class="section field-summary">

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

  `final `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a>`<`<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a>`<`[`GeoCoordinates`](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")`>>`

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-geopolygon#innerBoundaries"
  class="member-name-link"><code>innerBoundaries</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The list of polygon inner boundaries (holes), each defined as a list
  of geographic coordinates.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `final `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a>`<`[`GeoCoordinates`](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")`>`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-core-geopolygon#vertices"
  class="member-name-link"><code>vertices</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The list of geographic coordinates representing the outer boundary
  vertices of polygon.

  </div>

  </div>

  </div>

  </div>

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

      GeoPolygon(GeoBox geoBox)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Constructs an instance of this class from GeoBox .

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      GeoPolygon(GeoCircle geoCircle)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Constructs an instance of this class from GeoCircle .

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      GeoPolygon(List<GeoCoordinates> vertices)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Constructs an instance of this class from the provided vertices.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      GeoPolygon(List<GeoCoordinates> vertices,
       List<List<GeoCoordinates>> innerBoundaries)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Constructs an instance of this class from the provided vertices and
  inner boundaries (holes).

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

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      equals(Object obj)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      hashCode()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

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
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
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

- <div id="sdk-for-android-explore-field-detail"
  class="section field-details">

  - <div id="sdk-for-android-explore-vertices" class="section detail">

    ### vertices

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")></span> <span class="element-name">vertices</span>

    </div>

    <div class="block">

    The list of geographic coordinates representing the outer boundary
    vertices of polygon.

    </div>

    </div>

  - <div id="sdk-for-android-explore-innerBoundaries"
    class="section detail">

    ### innerBoundaries

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")>></span> <span class="element-name">innerBoundaries</span>

    </div>

    <div class="block">

    The list of polygon inner boundaries (holes), each defined as a list
    of geographic coordinates.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">

  - <div id="sdk-for-android-explore-<init>(java.util.List)"
    class="section detail">

    ### GeoPolygon

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">GeoPolygon</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")> vertices)</span>
    throws
    <span class="exceptions">[InstantiationErrorException](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")</span>

    </div>

    <div class="block">

    Constructs an instance of this class from the provided vertices.
    Throws InstantiationError if the number of vertices is less than
    three.

    </div>

    Parameters:  
    `vertices` -

    List of vertices representing the polygon outer boundary in
    clockwise order.

    Throws:  
    [`InstantiationErrorException`](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")

    Instantiation error.

    </div>

  - <div id="sdk-for-android-explore-<init>(java.util.List,java.util.List)"
    class="section detail">

    ### GeoPolygon

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">GeoPolygon</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")> vertices,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")>> innerBoundaries)</span>
    throws
    <span class="exceptions">[InstantiationErrorException](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")</span>

    </div>

    <div class="block">

    Constructs an instance of this class from the provided vertices and
    inner boundaries (holes). Throws InstantiationError if the number of
    vertices is less than three.

    </div>

    Parameters:  
    `vertices` -

    List of vertices representing the polygon outer boundary in
    clockwise order.

    `innerBoundaries` -

    List of polygon inner boundaries (holes), each in counterclockwise
    order.

    Throws:  
    [`InstantiationErrorException`](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")

    Instantiation error.

    </div>

  - <div id="sdk-for-android-explore-<init>(com.here.sdk.core.GeoCircle)"
    class="section detail">

    ### GeoPolygon

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">GeoPolygon</span><span class="parameters">(@NonNull
    [GeoCircle](sdk-for-android-explore-com-here-sdk-core-geocircle "class in com.here.sdk.core") geoCircle)</span>

    </div>

    <div class="block">

    Constructs an instance of this class from GeoCircle .

    </div>

    Parameters:  
    `geoCircle` -

    A
    [`GeoCircle`](sdk-for-android-explore-com-here-sdk-core-geocircle "class in com.here.sdk.core")
    to be converted into
    [`GeoPolygon`](sdk-for-android-explore-com-here-sdk-core-geopolygon "class in com.here.sdk.core").

    </div>

  - <div id="sdk-for-android-explore-<init>(com.here.sdk.core.GeoBox)"
    class="section detail">

    ### GeoPolygon

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">GeoPolygon</span><span class="parameters">(@NonNull
    [GeoBox](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core") geoBox)</span>

    </div>

    <div class="block">

    Constructs an instance of this class from GeoBox .

    </div>

    Parameters:  
    `geoBox` -

    A rectangle defined by the
    [`GeoBox`](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core")
    to be converted into
    [`GeoPolygon`](sdk-for-android-explore-com-here-sdk-core-geopolygon "class in com.here.sdk.core").
    The corner coordinates defined by the
    [`GeoBox`](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core")
    will define the outer boundary verticies of the
    [`GeoPolygon`](sdk-for-android-explore-com-here-sdk-core-geopolygon "class in com.here.sdk.core").

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-equals(java.lang.Object)"
    class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><span class="parameters">(<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
    class="external-link"
    title="class or interface in java.lang"><code>equals</code></a> in
    class <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link"
    title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-explore-hashCode()" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
    class="external-link"
    title="class or interface in java.lang"><code>hashCode</code></a> in
    class <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link"
    title="class or interface in java.lang"><code>Object</code></a>

    </div>

  </div>

</div>

