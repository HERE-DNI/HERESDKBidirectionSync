---
title: "Place (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-search-place"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.search](sdk-for-android-explore-com-here-sdk-search-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.NativeBasecom.here.sdk.search.Place →
com.here.NativeBase → com.here.sdk.search.Place

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">Place</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Represents a location object, such as a country, a city, a point of
interest (POI) etc.

</div>

</div>

<div class="section summary">

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Static Methods
  Instance Methods
  Concrete Methods

  </div>

  <div id="method-summary-table.tabpanel"
  aria-labelledby="method-summary-table-tab0" role="tabpanel">

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Method</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-search-place"
  title="class in com.here.sdk.search"><code>Place</code></a></td>
  <td><pre><code>deserialize(String serializedPlace)</code></pre></td>
  <td><div class="block">
  Returns a Place created from serialized string.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-core-geocoordinates"
  title="class in com.here.sdk.core"><code>GeoCoordinates</code></a><code>&gt;</code></td>
  <td><pre><code>getAccessPoints()</code></pre></td>
  <td><div class="block">
  Gets the access points to the place, such as the points on a road or in
  a parking lot.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-search-address"
  title="class in com.here.sdk.search"><code>Address</code></a></td>
  <td><pre><code>getAddress()</code></pre></td>
  <td><div class="block">
  Gets the address of the place.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-search-areatype"
  title="enum class in com.here.sdk.search"><code>AreaType</code></a></td>
  <td><pre><code>getAreaType()</code></pre></td>
  <td><div class="block">
  Gets the area type.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-geobox"
  title="class in com.here.sdk.core"><code>GeoBox</code></a></td>
  <td><pre><code>getBoundingBox()</code></pre></td>
  <td><div class="block">
  Gets the geographic coordinates of the bounding box containing the
  place.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-search-details"
  title="class in com.here.sdk.search"><code>Details</code></a></td>
  <td><pre><code>getDetails()</code></pre></td>
  <td><div class="block">
  Gets the place's detailed information.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
  class="external-link"
  title="class or interface in java.lang"><code>Integer</code></a></td>
  <td><pre><code>getDistanceInMeters()</code></pre></td>
  <td><div class="block">
  Gets the distance from the search center to the place in meters.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-geocoordinates"
  title="class in com.here.sdk.core"><code>GeoCoordinates</code></a></td>
  <td><pre><code>getGeoCoordinates()</code></pre></td>
  <td><div class="block">
  Gets the geographic coordinates of the place.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><pre><code>getId()</code></pre></td>
  <td><div class="block">
  Gets the unique id of this resource.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-search-placetype"
  title="enum class in com.here.sdk.search"><code>PlaceType</code></a></td>
  <td><pre><code>getPlaceType()</code></pre></td>
  <td><div class="block">
  Gets the place type.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><pre><code>getPoliticalView()</code></pre></td>
  <td><div class="block">
  Gets the geopolitical view, defined as a three letter country code, each
  disputed territory has international and alternative views.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><pre><code>getTitle()</code></pre></td>
  <td><div class="block">
  Gets the localized title for the resource.
  </div></td>
  </tr>
  <tr>
  <td><code>boolean</code></td>
  <td><pre><code>isCoordinatesInterpolated()</code></pre></td>
  <td><div class="block">
  Gets the flag saying whether the coordinates of the house number were
  interpolated or not.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><pre><code>serializeCompact()</code></pre></td>
  <td><div class="block">
  Serializes Place to persist or transfer.
  </div></td>
  </tr>
  </tbody>
  </table>

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

- <div id="method-detail" class="section method-details">

  - <div id="serializeCompact()" class="section detail">

    ### serializeCompact

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">serializeCompact</span>()

    </div>

    <div class="block">

    Serializes Place to persist or transfer. Preserves limited amount of
    data: getTitle() getId() getGeoCoordinates() getAccessPoints()
    getPlaceType() getBoundingBox() Details.getPrimaryCategories()
    Address.addressText Address.countryCode

    </div>

    Returns:  
    The serialized place

    </div>

  - <div id="deserialize(java.lang.String)" class="section detail">

    ### deserialize

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type">[Place](sdk-for-android-explore-com-here-sdk-search-place "class in com.here.sdk.search")</span> <span class="element-name">deserialize</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> serializedPlace)</span>
    throws
    <span class="exceptions">[PlaceSerializationException](sdk-for-android-explore-com-here-sdk-search-placeserializationexception "class in com.here.sdk.search")</span>

    </div>

    <div class="block">

    Returns a Place created from serialized string.

    </div>

    Parameters:  
    `serializedPlace` -

    The serialized place

    Returns:  
    A
    [`Place`](sdk-for-android-explore-com-here-sdk-search-place "class in com.here.sdk.search")
    created from serialized string.

    Throws:  
    [`PlaceSerializationException`](sdk-for-android-explore-com-here-sdk-search-placeserializationexception "class in com.here.sdk.search")
    -

    Indicates what went wrong during deserialization attempt.

    </div>

  - <div id="getTitle()" class="section detail">

    ### getTitle

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getTitle</span>()

    </div>

    <div class="block">

    Gets the localized title for the resource.

    </div>

    Returns:  
    The localized title for the resource.

    </div>

  - <div id="getId()" class="section detail">

    ### getId

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getId</span>()

    </div>

    <div class="block">

    Gets the unique id of this resource. It can be used to query further
    information. When returned from OfflineSearchEngine , id is valid
    only for Place objects whose place_type is POI . Otherwise, it is
    empty.

    </div>

    Returns:  
    The unique id of this resource. It can be used to query further
    information.

    </div>

  - <div id="getPlaceType()" class="section detail">

    ### getPlaceType

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[PlaceType](sdk-for-android-explore-com-here-sdk-search-placetype "enum class in com.here.sdk.search")</span> <span class="element-name">getPlaceType</span>()

    </div>

    <div class="block">

    Gets the place type.

    </div>

    Returns:  
    The place type.

    </div>

  - <div id="getAreaType()" class="section detail">

    ### getAreaType

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[AreaType](sdk-for-android-explore-com-here-sdk-search-areatype "enum class in com.here.sdk.search")</span> <span class="element-name">getAreaType</span>()

    </div>

    <div class="block">

    Gets the area type. It is available only when the getPlaceType() is
    PlaceType.AREA .

    </div>

    Returns:  
    The area type. It is available only when the
    [](sdk-for-android-explore-com-here-sdk-search-place#getPlaceType())

        getPlaceType()

    is
    [`PlaceType.AREA`](sdk-for-android-explore-com-here-sdk-search-placetype#AREA).

    </div>

  - <div id="getAddress()" class="section detail">

    ### getAddress

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[Address](sdk-for-android-explore-com-here-sdk-search-address "class in com.here.sdk.search")</span> <span class="element-name">getAddress</span>()

    </div>

    <div class="block">

    Gets the address of the place. Note that while
    OfflineSearchEngine.suggest and OfflineSearchEngine.suggestByText
    set all available details, SearchEngine.suggest and
    SearchEngine.suggestByText set only Address.addressText . Complete
    address details can be obtained by searching with PlaceIdQuery .

    </div>

    Returns:  
    The address of the place. Note that while
    `OfflineSearchEngine.suggest` and
    `OfflineSearchEngine.suggestByText` set all available details,
    `SearchEngine.suggest` and `SearchEngine.suggestByText` set only
    [`Address.addressText`](sdk-for-android-explore-com-here-sdk-search-address#addressText).
    Complete address details can be obtained by searching with
    [`PlaceIdQuery`](sdk-for-android-explore-com-here-sdk-search-placeidquery "class in com.here.sdk.search").

    </div>

  - <div id="getDetails()" class="section detail">

    ### getDetails

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[Details](sdk-for-android-explore-com-here-sdk-search-details "class in com.here.sdk.search")</span> <span class="element-name">getDetails</span>()

    </div>

    <div class="block">

    Gets the place's detailed information.

    </div>

    Returns:  
    The place's detailed information.

    </div>

  - <div id="getGeoCoordinates()" class="section detail">

    ### getGeoCoordinates

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")</span> <span class="element-name">getGeoCoordinates</span>()

    </div>

    <div class="block">

    Gets the geographic coordinates of the place. Can be null when
    retrieved from a suggestion's place property.

    </div>

    Returns:  
    The geographic coordinates of the place.

    </div>

  - <div id="isCoordinatesInterpolated()" class="section detail">

    ### isCoordinatesInterpolated

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isCoordinatesInterpolated</span>()

    </div>

    <div class="block">

    Gets the flag saying whether the coordinates of the house number
    were interpolated or not. This property is valid only for house
    number results retrieved using online search. When false, it means
    getGeoCoordinates() point to an accurate position of the house.
    Otherwise coordinates are slightly less accurate, but are based on a
    highly optimized interpolation algorithm.

    </div>

    Returns:  
    A property that says whether the coordinates of the house number
    were interpolated or not.

    </div>

  - <div id="getAccessPoints()" class="section detail">

    ### getAccessPoints

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")></span> <span class="element-name">getAccessPoints</span>()

    </div>

    <div class="block">

    Gets the access points to the place, such as the points on a road or
    in a parking lot. A place can have multiple access points. For
    example, a large warehouse can have multiple entrances, while the
    center of the warehouse may not be directly reachable. Note that
    access points are meant to be reachable by vehicles. For routes it
    is recommended to navigate to one of the available access points (if
    any), whereas the sideOfStreetHint should be set to the geographic
    coordinates of the place. The list is empty when no access points
    are known or when the place is directly reachable. A place can have
    multiple access points. For example, a large warehouse can have
    multiple entrances, while the center of the warehouse may not be
    directly reachable. Note that access points are meant to be
    reachable by vehicles. For routes it is recommended to navigate to
    one of the available access points (if any), whereas the
    sideOfStreetHint should be set to the geographic coordinates of the
    place. The list is empty when no access points are known or when the
    place is directly reachable.

    </div>

    Returns:  
    The access points to the place, such as the points on a road or in a
    parking lot.

    </div>

  - <div id="getBoundingBox()" class="section detail">

    ### getBoundingBox

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[GeoBox](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core")</span> <span class="element-name">getBoundingBox</span>()

    </div>

    <div class="block">

    Gets the geographic coordinates of the bounding box containing the
    place.

    </div>

    Returns:  
    The geographic coordinates of the map bounding box containing the
    place.

    </div>

  - <div id="getDistanceInMeters()" class="section detail">

    ### getDistanceInMeters

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html"
    class="external-link"
    title="class or interface in java.lang">Integer</a></span> <span class="element-name">getDistanceInMeters</span>()

    </div>

    <div class="block">

    Gets the distance from the search center to the place in meters.

    </div>

    Returns:  
    The distance from the search center to the place in meters.

    </div>

  - <div id="getPoliticalView()" class="section detail">

    ### getPoliticalView

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getPoliticalView</span>()

    </div>

    <div class="block">

    Gets the geopolitical view, defined as a three letter country code,
    each disputed territory has international and alternative views.
    Populated when the geopolitical view parameter is set in the
    SDKOptions and passed to SDKNativeEngine on instantiation, but only
    if it is an alternative view. For more details refer to SDKOptions .

    </div>

    Returns:  
    The geopolitical view, defined as a three letter country code, each
    disputed territory has international and alternative views.

    </div>

  </div>

</div>

