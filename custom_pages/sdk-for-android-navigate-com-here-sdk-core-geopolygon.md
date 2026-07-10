---
title: "GeoPolygon (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-geopolygon"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-core-package-summary">com.here.sdk.core</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.core.GeoPolygon → com.here.sdk.core.GeoPolygon

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">GeoPolygon</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Represents a GeoPolygon area as a series of geographic coordinates, and optionally, a list of inner boundaries (also known as holes). An instance of this class, initialized with appropriate vertices.

</div>

</div>

- <div id="sdk-for-android-navigate-field-summary" class="section field-summary">

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

  `final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">`GeoCoordinates`</a>`>>`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-core-geopolygon#innerBoundaries" class="member-name-link"><code>innerBoundaries</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The list of polygon inner boundaries (holes), each defined as a list of geographic coordinates.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">`GeoCoordinates`</a>`>`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-core-geopolygon#vertices" class="member-name-link"><code>vertices</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The list of geographic coordinates representing the outer boundary vertices of polygon.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-summary" class="section constructor-summary">

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

      GeoPolygon ( GeoBox geoBox)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Constructs an instance of this class from GeoBox .

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      GeoPolygon ( GeoCircle geoCircle)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Constructs an instance of this class from GeoCircle .

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      GeoPolygon ( List < GeoCoordinates > vertices)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Constructs an instance of this class from the provided vertices.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      GeoPolygon ( List < GeoCoordinates > vertices, List < List < GeoCoordinates >> innerBoundaries)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Constructs an instance of this class from the provided vertices and inner boundaries (holes).

  </div>

  </div>

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

- <div id="sdk-for-android-navigate-field-detail" class="section field-details">

  - <div id="sdk-for-android-navigate-vertices" class="section detail">

    ### vertices

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>\></span> <span class="element-name">vertices</span>

    </div>

    <div class="block">

    The list of geographic coordinates representing the outer boundary vertices of polygon.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-innerBoundaries" class="section detail">

    ### innerBoundaries

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>\>\></span> <span class="element-name">innerBoundaries</span>

    </div>

    <div class="block">

    The list of polygon inner boundaries (holes), each defined as a list of geographic coordinates.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-java-util-List" class="section detail">

    ### GeoPolygon

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">GeoPolygon</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>\> vertices)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Constructs an instance of this class from the provided vertices. Throws InstantiationError if the number of vertices is less than three.

    </div>

    Parameters:  
    `vertices` -

    List of vertices representing the polygon outer boundary in clockwise order.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> -

    Instantiation error.

    </div>

  - <div id="sdk-for-android-navigate-init-java-util-List-java-util-List" class="section detail">

    ### GeoPolygon

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">GeoPolygon</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>\> vertices, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>\>\> innerBoundaries)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Constructs an instance of this class from the provided vertices and inner boundaries (holes). Throws InstantiationError if the number of vertices is less than three.

    </div>

    Parameters:  
    `vertices` -

    List of vertices representing the polygon outer boundary in clockwise order.

    `innerBoundaries` -

    List of polygon inner boundaries (holes), each in counterclockwise order.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> -

    Instantiation error.

    </div>

  - <div id="sdk-for-android-navigate-init-com-here-sdk-core-GeoCircle" class="section detail">

    ### GeoPolygon

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">GeoPolygon</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-geocircle" title="class in com.here.sdk.core">GeoCircle</a> geoCircle)</span>

    </div>

    <div class="block">

    Constructs an instance of this class from GeoCircle .

    </div>

    Parameters:  
    `geoCircle` -

    A <a href="sdk-for-android-navigate-com-here-sdk-core-geocircle" title="class in com.here.sdk.core">`GeoCircle`</a> to be converted into <a href="sdk-for-android-navigate-com-here-sdk-core-geopolygon" title="class in com.here.sdk.core">`GeoPolygon`</a>.

    </div>

  - <div id="sdk-for-android-navigate-init-com-here-sdk-core-GeoBox" class="section detail">

    ### GeoPolygon

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">GeoPolygon</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a> geoBox)</span>

    </div>

    <div class="block">

    Constructs an instance of this class from GeoBox .

    </div>

    Parameters:  
    `geoBox` -

    A rectangle defined by the <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">`GeoBox`</a> to be converted into <a href="sdk-for-android-navigate-com-here-sdk-core-geopolygon" title="class in com.here.sdk.core">`GeoPolygon`</a>. The corner coordinates defined by the <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">`GeoBox`</a> will define the outer boundary verticies of the <a href="sdk-for-android-navigate-com-here-sdk-core-geopolygon" title="class in com.here.sdk.core">`GeoPolygon`</a>.

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-equals-java-lang-Object" class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr></wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-navigate-hashCode" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

