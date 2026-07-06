---
title: "MapView.ViewPin (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapview-viewpin"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

Enclosing class:  
[MapView](sdk-for-android-explore-com-here-sdk-mapview-mapview "class in com.here.sdk.mapview")

<div class="type-signature">

<span class="modifiers">public static interface
</span><span class="element-name type-name-label">MapView.ViewPin</span>

</div>

<div class="block">

A ViewPin is used to display Android views at a fixed location on the
map. The pinned view will automatically be repositioned on the screen as
the map moves. There is more performance overhead involved in
positioning a pinned view as compared to a map marker, so for use cases
which only require static images, markers should be used.

</div>

</div>

<div class="section summary">
<div id="sdk-for-android-explore-method-summary"
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

  [`Anchor2D`](sdk-for-android-explore-com-here-sdk-core-anchor2d "class in com.here.sdk.core")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getAnchorPoint()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets anchor point for this instance.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  [`GeoCoordinates`](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getGeoCoordinates()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Returns the current GeoCoordinates on the map.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setAnchorPoint(Anchor2D anchorPoint)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets an anchor point for this instance.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setGeoCoordinates(GeoCoordinates geoCoordinates)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets the GeoCoordinates on the map.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      unpin()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Removes the view from the MapView it was pinned to.

  </div>

  </div>

  </div>

  </div>

  </div>

</div>

<div class="section details">
<div id="sdk-for-android-explore-method-detail"
  class="section method-details">
<div id="sdk-for-android-explore-unpin()" class="section detail">

    ### unpin

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">unpin</span>()

    </div>

    <div class="block">

    Removes the view from the MapView it was pinned to.

    </div>

    </div>
<div id="sdk-for-android-explore-getGeoCoordinates()"
    class="section detail">

    ### getGeoCoordinates

    <div class="member-signature">

    <span class="return-type">[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")</span> <span class="element-name">getGeoCoordinates</span>()

    </div>

    <div class="block">

    Returns the current GeoCoordinates on the map.

    </div>

    Returns:  
    The current GeoCoordinates.

    </div>
<div id="sdk-for-android-explore-setGeoCoordinates(com.here.sdk.core.GeoCoordinates)"
    class="section detail">

    ### setGeoCoordinates

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setGeoCoordinates</span><span class="parameters">(@NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") geoCoordinates)</span>

    </div>

    <div class="block">

    Sets the GeoCoordinates on the map. The altitude component of the
    coordinates, if set, is interpreted as above sea level. When not
    set, the coordinates are interpreted as at ground level.

    </div>

    Parameters:  
    `geoCoordinates` - Desired GeoCoordinates for this view pin.

    </div>
<div id="sdk-for-android-explore-setAnchorPoint(com.here.sdk.core.Anchor2D)"
    class="section detail">

    ### setAnchorPoint

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setAnchorPoint</span><span class="parameters">(@NonNull
    [Anchor2D](sdk-for-android-explore-com-here-sdk-core-anchor2d "class in com.here.sdk.core") anchorPoint)</span>

    </div>

    <div class="block">

    Sets an anchor point for this instance. The anchor value has valid
    range from 0 to 1. Zero (0) for x and y means the view pin's upper
    left corner is located at the geographical location, whereas one (1)
    for x and y means that the pin will have its right bottom corner
    attached to the geographical location instead. The default value
    used is 0.5, 0.5, causing the view to be centered.

    </div>

    Parameters:  
    `anchorPoint` - A `Anchor2D` relative to the top-left corner of the
    `ViewPin`.

    </div>
<div id="sdk-for-android-explore-getAnchorPoint()"
    class="section detail">

    ### getAnchorPoint

    <div class="member-signature">

    <span class="return-type">[Anchor2D](sdk-for-android-explore-com-here-sdk-core-anchor2d "class in com.here.sdk.core")</span> <span class="element-name">getAnchorPoint</span>()

    </div>

    <div class="block">

    Gets anchor point for this instance.

    </div>

    Returns:  
    anchorPoint A `Anchor2D` relative to the top-left corner of the
    ` ViewPin`.

    </div>

  </div>

</div>

