---
title: "Venue (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-control-venue"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-venue-control-package-summary">com.here.sdk.venue.control</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.venue.control.Venue → com.here.NativeBase com.here.sdk.venue.control.Venue → com.here.sdk.venue.control.Venue

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">Venue</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span>

</div>

<div class="block">

Controls the VenueModel inside the VenueMap object. The venue controls the selection of the VenueDrawing and the VenueLevel of the VenueModel . It provides the possibility to customize styles for the VenueGeometry . Objects of this class can only be created using methods VenueMap.addVenueAsync(String, VenueLoadErrorCallback) and VenueMap.selectVenueAsync(String, VenueLoadErrorCallback) .

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

  <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data">`VenueDrawing`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getSelectedDrawing ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the currently selected VenueDrawing of the VenueModel .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data">`VenueLevel`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getSelectedLevel ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the currently selected VenueLevel from the selected VenueDrawing .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getSelectedLevelIndex ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the index of the currently selected VenueLevel in the level array of the related VenueDrawing .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getSelectedLevelZIndex ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the Z index of the currently selected VenueLevel .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel" title="class in com.here.sdk.venue.data">`VenueModel`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getVenueModel ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the VenueModel controlled by this object.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-venue-style-venuestyle" title="class in com.here.sdk.venue.style">`VenueStyle`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getVenueStyle ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the VenueStyle associated with the VenueModel controlled by this object.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      isTopologyVisible ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the current status of topology visibility.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setCustomStyle ( List < VenueGeometry > geometries, VenueGeometryStyle style, VenueLabelStyle labelStyle)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets a custom style for geometries and related labels.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setCustomStyle ( List < VenueTopology > topologies, VenueGeometryStyle style)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets a custom style for topologies.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setCustomStyleToCrosswalk ( List < Crosswalk > crosswalks, VenueGeometryStyle style)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets a custom style for crosswalk.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setSelectedDrawing ( VenueDrawing value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the selected VenueDrawing .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setSelectedLevel ( VenueLevel value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the selected VenueLevel from the currently selected VenueDrawing .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setSelectedLevelIndex (int value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the VenueLevel with the specified index from the level array of the VenueDrawing as selected.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setSelectedLevelZIndex (int value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the VenueLevel with the specified Z index as selected.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setTopologyVisible (boolean value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the topology visibility.

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

  - <div id="sdk-for-android-navigate-setCustomStyle-java-util-List-com-here-sdk-venue-style-VenueGeometryStyle-com-here-sdk-venue-style-VenueLabelStyle" class="section detail">

    ### setCustomStyle

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCustomStyle</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a>\> geometries, @Nullable <a href="sdk-for-android-navigate-com-here-sdk-venue-style-venuegeometrystyle" title="class in com.here.sdk.venue.style">VenueGeometryStyle</a> style, @Nullable <a href="sdk-for-android-navigate-com-here-sdk-venue-style-venuelabelstyle" title="class in com.here.sdk.venue.style">VenueLabelStyle</a> labelStyle)</span>

    </div>

    <div class="block">

    Sets a custom style for geometries and related labels.

    </div>

    Parameters:  
    `geometries` -

    The list of geometries to apply the new style.

    `style` -

    The style for geometries, or `null` to reset the style to default.

    `labelStyle` -

    The style for geometry labels, or `null` to reset the label style to default.

    </div>

  - <div id="sdk-for-android-navigate-setCustomStyle-java-util-List-com-here-sdk-venue-style-VenueGeometryStyle" class="section detail">

    ### setCustomStyle

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCustomStyle</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuetopology" title="class in com.here.sdk.venue.data">VenueTopology</a>\> topologies, @Nullable <a href="sdk-for-android-navigate-com-here-sdk-venue-style-venuegeometrystyle" title="class in com.here.sdk.venue.style">VenueGeometryStyle</a> style)</span>

    </div>

    <div class="block">

    Sets a custom style for topologies.

    </div>

    Parameters:  
    `topologies` -

    The list of topologies to apply the new style.

    `style` -

    The style for geometries, or `null` to reset the style to default.

    </div>

  - <div id="sdk-for-android-navigate-setCustomStyleToCrosswalk-java-util-List-com-here-sdk-venue-style-VenueGeometryStyle" class="section detail">

    ### setCustomStyleToCrosswalk

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCustomStyleToCrosswalk</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-venue-data-crosswalk" title="class in com.here.sdk.venue.data">Crosswalk</a>\> crosswalks, @Nullable <a href="sdk-for-android-navigate-com-here-sdk-venue-style-venuegeometrystyle" title="class in com.here.sdk.venue.style">VenueGeometryStyle</a> style)</span>

    </div>

    <div class="block">

    Sets a custom style for crosswalk.

    </div>

    Parameters:  
    `crosswalks` -

    The list of crosswalk to apply the new style.

    `style` -

    The style for geometries, or `null` to reset the style to default.

    </div>

  - <div id="sdk-for-android-navigate-getVenueModel" class="section detail">

    ### getVenueModel

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel" title="class in com.here.sdk.venue.data">VenueModel</a></span> <span class="element-name">getVenueModel</span>()

    </div>

    <div class="block">

    Gets the VenueModel controlled by this object. It can be used to get the VenueModel belonging to this object, like a building or a complex of buildings.

    </div>

    Returns:  
    The <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel" title="class in com.here.sdk.venue.data">`VenueModel`</a> controlled by this object.

    </div>

  - <div id="sdk-for-android-navigate-getVenueStyle" class="section detail">

    ### getVenueStyle

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-style-venuestyle" title="class in com.here.sdk.venue.style">VenueStyle</a></span> <span class="element-name">getVenueStyle</span>()

    </div>

    <div class="block">

    Gets the VenueStyle associated with the VenueModel controlled by this object. It can be used to get the style of the venue. Contains the information about the geometry and label styles available for the venue.

    </div>

    Returns:  
    The <a href="sdk-for-android-navigate-com-here-sdk-venue-style-venuestyle" title="class in com.here.sdk.venue.style">`VenueStyle`</a> associated with the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel" title="class in com.here.sdk.venue.data">`VenueModel`</a> controlled by this object.

    </div>

  - <div id="sdk-for-android-navigate-getSelectedDrawing" class="section detail">

    ### getSelectedDrawing

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data">VenueDrawing</a></span> <span class="element-name">getSelectedDrawing</span>()

    </div>

    <div class="block">

    Gets the currently selected VenueDrawing of the VenueModel . Only the selected drawing will be visible as active on the map. All others will be hidden or displayed without details, depending on the implementation of the renderer.

    </div>

    Returns:  
    The selected drawing.

    </div>

  - <div id="sdk-for-android-navigate-setSelectedDrawing-com-here-sdk-venue-data-VenueDrawing" class="section detail">

    ### setSelectedDrawing

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSelectedDrawing</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data">VenueDrawing</a> value)</span>

    </div>

    <div class="block">

    Sets the selected VenueDrawing . Only the selected drawing will be visible as active on the map. All others will be hidden or displayed without details, depending on the implementation of the renderer.

    </div>

    Parameters:  
    `value` -

    The selected drawing.

    </div>

  - <div id="sdk-for-android-navigate-getSelectedLevel" class="section detail">

    ### getSelectedLevel

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data">VenueLevel</a></span> <span class="element-name">getSelectedLevel</span>()

    </div>

    <div class="block">

    Gets the currently selected VenueLevel from the selected VenueDrawing . Only the selected level will be visible as active on the map. All others will be hidden or displayed without details, depending on a renderer implementation. If the level doesn't belong to the currently selected drawing, it can not be selected.

    </div>

    Returns:  
    The selected level.

    </div>

  - <div id="sdk-for-android-navigate-setSelectedLevel-com-here-sdk-venue-data-VenueLevel" class="section detail">

    ### setSelectedLevel

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSelectedLevel</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data">VenueLevel</a> value)</span>

    </div>

    <div class="block">

    Sets the selected VenueLevel from the currently selected VenueDrawing . Only the selected level will be visible as active on the map. All others will be hidden or displayed without details, depending on a renderer implementation. If the level doesn't belong to the currently selected drawing, it can not be selected.

    </div>

    Parameters:  
    `value` -

    The selected level.

    </div>

  - <div id="sdk-for-android-navigate-getSelectedLevelZIndex" class="section detail">

    ### getSelectedLevelZIndex

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getSelectedLevelZIndex</span>()

    </div>

    <div class="block">

    Gets the Z index of the currently selected VenueLevel . Z index 0 represents the ground level, negative values represent underground levels, positive values - levels above the ground. Z index can also be taken from VenueLevel.getZIndex() .

    </div>

    Returns:  
    The Z index value of the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data">`VenueLevel`</a> selected.

    </div>

  - <div id="sdk-for-android-navigate-setSelectedLevelZIndex-int" class="section detail">

    ### setSelectedLevelZIndex

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSelectedLevelZIndex</span><wbr></wbr><span class="parameters">(int value)</span>

    </div>

    <div class="block">

    Sets the VenueLevel with the specified Z index as selected. Z index 0 represents the ground level, negative values represent underground levels, positive values - levels above the ground. Z index can also be taken from VenueLevel.getZIndex() .

    </div>

    Parameters:  
    `value` -

    The Z index value of the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data">`VenueLevel`</a> selected.

    </div>

  - <div id="sdk-for-android-navigate-getSelectedLevelIndex" class="section detail">

    ### getSelectedLevelIndex

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getSelectedLevelIndex</span>()

    </div>

    <div class="block">

    Gets the index of the currently selected VenueLevel in the level array of the related VenueDrawing . The level array can be taken from VenueDrawing.getLevels() . Unlike the Z index, it can't have a negative value.

    </div>

    Returns:  
    The index of the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data">`VenueLevel`</a> selected from the level array of the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data">`VenueDrawing`</a>.

    </div>

  - <div id="sdk-for-android-navigate-setSelectedLevelIndex-int" class="section detail">

    ### setSelectedLevelIndex

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSelectedLevelIndex</span><wbr></wbr><span class="parameters">(int value)</span>

    </div>

    <div class="block">

    Sets the VenueLevel with the specified index from the level array of the VenueDrawing as selected. Unlike the Z index, it can't have a negative value.

    </div>

    Parameters:  
    `value` -

    The index of the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data">`VenueLevel`</a> selected from the level array of the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data">`VenueDrawing`</a>.

    </div>

  - <div id="sdk-for-android-navigate-isTopologyVisible" class="section detail">

    ### isTopologyVisible

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTopologyVisible</span>()

    </div>

    <div class="block">

    Gets the current status of topology visibility. It can be used to check the status of topology visibility.

    </div>

    Returns:  
    Returns true if topology is visible.

    </div>

  - <div id="sdk-for-android-navigate-setTopologyVisible-boolean" class="section detail">

    ### setTopologyVisible

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTopologyVisible</span><wbr></wbr><span class="parameters">(boolean value)</span>

    </div>

    <div class="block">

    Sets the topology visibility. It can be used to check the status of topology visibility.

    </div>

    Parameters:  
    `value` -

    Returns true if topology is visible.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

