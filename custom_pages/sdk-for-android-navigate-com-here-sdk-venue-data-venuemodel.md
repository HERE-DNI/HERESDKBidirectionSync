---
title: "VenueModel (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-venue-data-package-summary">com.here.sdk.venue.data</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.venue.data.VenueModel → com.here.NativeBase com.here.sdk.venue.data.VenueModel → com.here.sdk.venue.data.VenueModel

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">VenueModel</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span>

</div>

<div class="block">

Represents a building or a complex of buildings, like airports or universities.

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

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry" title="class in com.here.sdk.venue.data">`VenueGeometry`</a>`>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      filterGeometry ( String filter, VenueGeometryFilterType filterType)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the filtered geometries in an ascending order.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">`GeoBox`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getBoundingBox ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets a bounding box of the venue model.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">`GeoCoordinates`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getCenter ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets a center of the venue model.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data">`VenueDrawing`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getDrawing (int drawingId)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets a drawing for a given drawing id.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data">`VenueDrawing`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getDrawing ( String drawingId)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets a drawing for a given drawing id.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data">`VenueDrawing`</a>`>`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getDrawings ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the drawings of the venue model.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry" title="class in com.here.sdk.venue.data">`VenueGeometry`</a>`>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getGeometries ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets a list of geometries of the venue.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" class="external-link" title="class or interface in java.util"><code>Map</code></a>`<`<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>, <wbr></wbr><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry" title="class in com.here.sdk.venue.data">`VenueGeometry`</a>`>>`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getGeometriesByIconNames ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets geometries mapped by icon names.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry" title="class in com.here.sdk.venue.data">`VenueGeometry`</a>`>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getGeometriesByName ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the geometries ordered by the name in an ascending order.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getId ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets an id of the venue model.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getIdentifier ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets an id of the venue model.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getLanguage ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets a language of the venue model.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" class="external-link" title="class or interface in java.util"><code>Map</code></a>`<`<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>, <wbr></wbr><a href="sdk-for-android-navigate-com-here-sdk-venue-data-property" title="class in com.here.sdk.venue.data">`Property`</a>`>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getProperties ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets properties of the venue model.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuetopology" title="class in com.here.sdk.venue.data">`VenueTopology`</a>`>`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTopologies ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets a list of topologies of the drawing.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-getDrawing-int" class="section detail">

    ### getDrawing

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data">VenueDrawing</a></span> <span class="element-name">getDrawing</span><wbr></wbr><span class="parameters">(int drawingId)</span>

    </div>

    <div class="block">

    Gets a drawing for a given drawing id.

    </div>

    Parameters:  
    `drawingId` -

    The id of the drawing.

    Returns:  
    The drawing with the given id or `null`.

    </div>

  - <div id="sdk-for-android-navigate-getDrawing-java-lang-String" class="section detail">

    ### getDrawing

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data">VenueDrawing</a></span> <span class="element-name">getDrawing</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> drawingId)</span>

    </div>

    <div class="block">

    Gets a drawing for a given drawing id.

    </div>

    Parameters:  
    `drawingId` -

    The id of the drawing.

    Returns:  
    The drawing with the given id or `null`.

    </div>

  - <div id="sdk-for-android-navigate-filterGeometry-java-lang-String-com-here-sdk-venue-data-VenueGeometryFilterType" class="section detail">

    ### filterGeometry

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a>\></span> <span class="element-name">filterGeometry</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> filter, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometryfiltertype" title="enum class in com.here.sdk.venue.data">VenueGeometryFilterType</a> filterType)</span>

    </div>

    <div class="block">

    Gets the filtered geometries in an ascending order.

    </div>

    Parameters:  
    `filter` -

    The filter string.

    `filterType` -

    The filter type.

    Returns:  
    The list of the filtered geometries or an empty list.

    </div>

  - <div id="sdk-for-android-navigate-getId" class="section detail">

    ### getId

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getId</span>()

    </div>

    <div class="block">

    Gets an id of the venue model.

    </div>

    Returns:  
    The `id` of the venue model.

    </div>

  - <div id="sdk-for-android-navigate-getIdentifier" class="section detail">

    ### getIdentifier

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getIdentifier</span>()

    </div>

    <div class="block">

    Gets an id of the venue model.

    </div>

    Returns:  
    The `id` of the venue model.

    </div>

  - <div id="sdk-for-android-navigate-getCenter" class="section detail">

    ### getCenter

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span class="element-name">getCenter</span>()

    </div>

    <div class="block">

    Gets a center of the venue model.

    </div>

    Returns:  
    The geographic coordinates of the center of the venue model.

    </div>

  - <div id="sdk-for-android-navigate-getBoundingBox" class="section detail">

    ### getBoundingBox

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a></span> <span class="element-name">getBoundingBox</span>()

    </div>

    <div class="block">

    Gets a bounding box of the venue model.

    </div>

    Returns:  
    The `GeoBox` of the bounding area of the venue model.

    </div>

  - <div id="sdk-for-android-navigate-getDrawings" class="section detail">

    ### getDrawings

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data">VenueDrawing</a>\></span> <span class="element-name">getDrawings</span>()

    </div>

    <div class="block">

    Gets the drawings of the venue model.

    </div>

    Returns:  
    The array of the Drawing objects.

    </div>

  - <div id="sdk-for-android-navigate-getProperties" class="section detail">

    ### getProperties

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" class="external-link" title="class or interface in java.util">Map</a>\<<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a>,<wbr></wbr><a href="sdk-for-android-navigate-com-here-sdk-venue-data-property" title="class in com.here.sdk.venue.data">Property</a>\></span> <span class="element-name">getProperties</span>()

    </div>

    <div class="block">

    Gets properties of the venue model.

    </div>

    Returns:  
    The properties of the venue model.

    </div>

  - <div id="sdk-for-android-navigate-getLanguage" class="section detail">

    ### getLanguage

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getLanguage</span>()

    </div>

    <div class="block">

    Gets a language of the venue model.

    </div>

    Returns:  
    The language of the venue model.

    </div>

  - <div id="sdk-for-android-navigate-getGeometriesByName" class="section detail">

    ### getGeometriesByName

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a>\></span> <span class="element-name">getGeometriesByName</span>()

    </div>

    <div class="block">

    Gets the geometries ordered by the name in an ascending order.

    </div>

    Returns:  
    The geometries ordered by the name in an ascending order.

    </div>

  - <div id="sdk-for-android-navigate-getGeometriesByIconNames" class="section detail">

    ### getGeometriesByIconNames

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" class="external-link" title="class or interface in java.util">Map</a>\<<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a>,<wbr></wbr><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a>\>\></span> <span class="element-name">getGeometriesByIconNames</span>()

    </div>

    <div class="block">

    Gets geometries mapped by icon names.

    </div>

    Returns:  
    The map from the icon names to the geometries in the drawing.

    </div>

  - <div id="sdk-for-android-navigate-getTopologies" class="section detail">

    ### getTopologies

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuetopology" title="class in com.here.sdk.venue.data">VenueTopology</a>\></span> <span class="element-name">getTopologies</span>()

    </div>

    <div class="block">

    Gets a list of topologies of the drawing.

    </div>

    Returns:  
    The list of topologies of the drawing.

    </div>

  - <div id="sdk-for-android-navigate-getGeometries" class="section detail">

    ### getGeometries

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a>\></span> <span class="element-name">getGeometries</span>()

    </div>

    <div class="block">

    Gets a list of geometries of the venue.

    </div>

    Returns:  
    The list of geometries of the venue or an empty list if no geometry present for venue.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

