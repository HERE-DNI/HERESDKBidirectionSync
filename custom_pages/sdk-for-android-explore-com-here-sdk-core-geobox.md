---
title: "GeoBox (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-geobox"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-com-here-sdk-core-package-summary">com.here.sdk.core</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.core.GeoBox → com.here.sdk.core.GeoBox

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">GeoBox</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Represents a bounding rectangle aligned with latitude and longitude. Geographic area represented by this would be visualised as a rectangle when using a normal cylindrical projection (such as Mercator). The box has a maximum span of 360 degrees in longitude and 180 degrees in latitude direction. The box with equal values in longitude for the corners is considered as a span of 360 degrees. The box is considered empty if the latitude of the southWestCorner is larger than the the latitude of the northEastCorner .

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

  `final `<a href="sdk-for-android-explore-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">`GeoCoordinates`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-core-geobox#northEastCorner" class="member-name-link"><code>northEastCorner</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  North east corner coordinates.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `final `<a href="sdk-for-android-explore-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">`GeoCoordinates`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-core-geobox#southWestCorner" class="member-name-link"><code>southWestCorner</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  South west corner coordinates.

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

      GeoBox ( GeoCoordinates southWestCorner, GeoCoordinates northEastCorner)

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="sdk-for-android-explore-com-here-sdk-core-geobox" title="class in com.here.sdk.core">`GeoBox`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      containing ( List < GeoCoordinates > geoCoordinates)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Creates a GeoBox which encompases all coordinates from the list.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      contains ( GeoBox geoBox)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Determines whether the specified GeoBox is covered entirely by this GeoBox .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      contains ( GeoCoordinates geoCoordinates)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Determines whether the specified GeoCoordinates is contained within this GeoBox .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-explore-com-here-sdk-core-geobox" title="class in com.here.sdk.core">`GeoBox`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      envelope ( GeoBox geoBox)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Envelopes two GeoBox areas by returning the smallest GeoBox covering both this GeoBox and the specified GeoBox .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="sdk-for-android-explore-com-here-sdk-core-geobox" title="class in com.here.sdk.core">`GeoBox`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      envelopeGeoBoxes ( List < GeoBox > geoBoxes)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Envelopes the list of GeoBox areas by returning the smallest GeoBox covering all specified GeoBox objects.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      equals ( Object obj)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-explore-com-here-sdk-core-geobox" title="class in com.here.sdk.core">`GeoBox`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      expandedBy (double southMeters,
       double westMeters,
       double northMeters,
       double eastMeters)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Creates a GeoBox which is expanded by a fixed distance.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      hashCode ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-explore-com-here-sdk-core-geobox" title="class in com.here.sdk.core">`GeoBox`</a>`>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      intersection ( GeoBox geoBox)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Computes the intersection with the passed GeoBox .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-explore-com-here-sdk-core-geobox" title="class in com.here.sdk.core">`GeoBox`</a>`>`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      intersection ( List < GeoBox > geoBoxes)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Computes intersection of list of GeoBox instances.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      intersects ( GeoBox geoBox)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Determines whether this GeoBox intersects with the passed GeoBox .

  </div>

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

  - <div id="sdk-for-android-explore-southWestCorner" class="section detail">

    ### southWestCorner

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span class="element-name">southWestCorner</span>

    </div>

    <div class="block">

    South west corner coordinates.

    </div>

    </div>

  - <div id="sdk-for-android-explore-northEastCorner" class="section detail">

    ### northEastCorner

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span class="element-name">northEastCorner</span>

    </div>

    <div class="block">

    North east corner coordinates.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-explore-init-com-here-sdk-core-GeoCoordinates-com-here-sdk-core-GeoCoordinates" class="section detail">

    ### GeoBox

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">GeoBox</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-explore-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> southWestCorner, @NonNull <a href="sdk-for-android-explore-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> northEastCorner)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `southWestCorner` -

    South west corner coordinates.

    `northEastCorner` -

    North east corner coordinates.

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

  - <div id="sdk-for-android-explore-containing-java-util-List" class="section detail">

    ### containing

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a></span> <span class="element-name">containing</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-explore-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>\> geoCoordinates)</span>

    </div>

    <div class="block">

    Creates a GeoBox which encompases all coordinates from the list. The provided list must contain at least two points. The altitude values of the input coordinates are not considered for the result.

    </div>

    Parameters:  
    `geoCoordinates` -

    List of coordinates to encompass inside bounding box.

    Returns:  
    `GeoBox` containing all supplied coordinates, or `null` if less than two coordinates were provided.

    </div>

  - <div id="sdk-for-android-explore-envelope-com-here-sdk-core-GeoBox" class="section detail">

    ### envelope

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a></span> <span class="element-name">envelope</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-explore-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a> geoBox)</span>

    </div>

    <div class="block">

    Envelopes two GeoBox areas by returning the smallest GeoBox covering both this GeoBox and the specified GeoBox .

    </div>

    Parameters:  
    `geoBox` -

    Another `GeoBox` to envelope with.

    Returns:  
    `GeoBox` covering two`GeoBox` areas

    </div>

  - <div id="sdk-for-android-explore-envelopeGeoBoxes-java-util-List" class="section detail">

    ### envelopeGeoBoxes

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a></span> <span class="element-name">envelopeGeoBoxes</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-explore-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a>\> geoBoxes)</span>

    </div>

    <div class="block">

    Envelopes the list of GeoBox areas by returning the smallest GeoBox covering all specified GeoBox objects.

    </div>

    Parameters:  
    `geoBoxes` -

    List of `GeoBox` objects.

    Returns:  
    `GeoBox` covering all `GeoBox` areas, or `null` if input is empty.

    </div>

  - <div id="sdk-for-android-explore-intersects-com-here-sdk-core-GeoBox" class="section detail">

    ### intersects

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">intersects</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-explore-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a> geoBox)</span>

    </div>

    <div class="block">

    Determines whether this GeoBox intersects with the passed GeoBox . The altitude values are ignored.

    </div>

    Parameters:  
    `geoBox` -

    A `GeoBox` to check for intersection.

    Returns:  
    `true` if intersects with the `GeoBox, false` otherwise.

    </div>

  - <div id="sdk-for-android-explore-intersection-com-here-sdk-core-GeoBox" class="section detail">

    ### intersection

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-explore-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a>\></span> <span class="element-name">intersection</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-explore-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a> geoBox)</span>

    </div>

    <div class="block">

    Computes the intersection with the passed GeoBox . The altitude values are ignored. Limitation: Geo boxes are considered as non-intersecting if they overlap only on a single point, horizontal line or vertical line. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    </div>

    Parameters:  
    `geoBox` -

    Another geo box to check intersection with.

    Returns:  
    It will be empty if there is no overlap. Otherwise, 1 or more geo boxes covering common area by this and passed <a href="sdk-for-android-explore-com-here-sdk-core-geobox" title="class in com.here.sdk.core">`GeoBox`</a>.

    </div>

  - <div id="sdk-for-android-explore-intersection-java-util-List" class="section detail">

    ### intersection

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public static</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-explore-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a>\></span> <span class="element-name">intersection</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-explore-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a>\> geoBoxes)</span>

    </div>

    <div class="block">

    Computes intersection of list of GeoBox instances. The altitude values are ignored. Limitation: Geo boxes are considered as non-intersecting if they overlap only on a single point, horizontal line or vertical line. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    </div>

    Parameters:  
    `geoBoxes` -

    List of <a href="sdk-for-android-explore-com-here-sdk-core-geobox" title="class in com.here.sdk.core">`GeoBox`</a> instances.

    Returns:  
    It will be empty if there is no overlap between all the passed <a href="sdk-for-android-explore-com-here-sdk-core-geobox" title="class in com.here.sdk.core">`GeoBox`</a> instances. Otherwise, 1 or more geo boxes covering common area by all the passed <a href="sdk-for-android-explore-com-here-sdk-core-geobox" title="class in com.here.sdk.core">`GeoBox`</a> instances.

    </div>

  - <div id="sdk-for-android-explore-contains-com-here-sdk-core-GeoBox" class="section detail">

    ### contains

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">contains</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-explore-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a> geoBox)</span>

    </div>

    <div class="block">

    Determines whether the specified GeoBox is covered entirely by this GeoBox . The altitude values are ignored.

    </div>

    Parameters:  
    `geoBox` -

    A `GeoBox` to check for containment within this `GeoBox`.

    Returns:  
    `true` if covered by the `GeoBox, false` otherwise.

    </div>

  - <div id="sdk-for-android-explore-contains-com-here-sdk-core-GeoCoordinates" class="section detail">

    ### contains

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">contains</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-explore-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> geoCoordinates)</span>

    </div>

    <div class="block">

    Determines whether the specified GeoCoordinates is contained within this GeoBox . The altitude values are ignored.

    </div>

    Parameters:  
    `geoCoordinates` -

    A GeoCoordinates to check for containment within this `GeoBox`.

    Returns:  
    `true` if contained within the `GeoBox, false` otherwise.

    </div>

  - <div id="sdk-for-android-explore-expandedBy-double-double-double-double" class="section detail">

    ### expandedBy

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a></span> <span class="element-name">expandedBy</span><wbr></wbr><span class="parameters">(double southMeters, double westMeters, double northMeters, double eastMeters)</span> throws <span class="exceptions"><a href="sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Creates a GeoBox which is expanded by a fixed distance. Throws an InstantiationError if it is not possible to create a valid GeoBox with the given arguments.

    </div>

    Parameters:  
    `southMeters` -

    Distance in the south direction in meters to expand the `GeoBox`.

    `westMeters` -

    Distance in the west direction in meters to expand the `GeoBox`.

    `northMeters` -

    Distance in the north direction in meters to expand the `GeoBox`.

    `eastMeters` -

    Distance in the east direction in meters to expand the `GeoBox`.

    Returns:  
    The expanded `GeoBox`.

    Throws:  
    <a href="sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> -

    Instantiation error.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

