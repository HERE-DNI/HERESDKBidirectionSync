---
title: "VenueMap (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-control-venuemap"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-venue-control-package-summary">com.here.sdk.venue.control</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.venue.control.VenueMap → com.here.NativeBase com.here.sdk.venue.control.VenueMap → com.here.sdk.venue.control.VenueMap

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">VenueMap</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span>

</div>

<div class="block">

Connects a map with venues. When the VenueMap is started, venues can be seen on the map as interactive models. The user can switch drawings and levels, change a visual style of geometries and related labels inside the venue etc. After constructing the VenueMap , listeners for relevant events should be added to the object. VenueMap is an add-on to the base map functionality with its own content loading and cache. For this reason, in certain situations there may be a small delay before the venue is visible.

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

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      add ( VenueDrawingSelectionListener listener)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Adds a drawing selection listener.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      add ( VenueInfoListListener listener)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Adds a listener to handle the completion of the asynchronous venue info list retrieval.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      add ( VenueLevelSelectionListener listener)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Adds a level selection listener.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      add ( VenueLifecycleListener listener)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Adds a venue lifecycle listener.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      add ( VenueMapLifecycleListener listener)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Adds a venue map lifecycle listener.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      add ( VenueSelectionListener listener)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Adds a venue selection listener.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      addVenueAsync (int venueId)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Downloads and adds a Venue to the VenueMap .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      addVenueAsync (int venueId, VenueLoadErrorCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Downloads and adds a Venue to the VenueMap .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      addVenueAsync ( String venueIdentifier)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Downloads and adds a Venue to the VenueMap .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      addVenueAsync ( String venueIdentifier, VenueLoadErrorCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Downloads and adds a Venue to the VenueMap .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      cancelVenueSelection ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Attempts to cancel venue loading and selection that may currently be in progress.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-venue-data-crosswalk" title="class in com.here.sdk.venue.data">`Crosswalk`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getCrosswalk ( GeoCoordinates position)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Tries to find a Crosswalk at the specified geographic coordinates in the selected Venue in the currently selected VenueLevel .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry" title="class in com.here.sdk.venue.data">`VenueGeometry`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getGeometry ( GeoCoordinates position)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Tries to find a VenueGeometry at the specified geographic coordinates in the selected Venue in the currently selected VenueLevel .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control">`Venue`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getSelectedVenue ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the currently selected Venue .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuetopology" title="class in com.here.sdk.venue.data">`VenueTopology`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTopology ( GeoCoordinates position)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Tries to find a VenueTopology at the specified geographic coordinates in the selected Venue in the currently selected VenueLevel .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control">`Venue`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getVenue ( GeoCoordinates position)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Tries to find a Venue at the specified geographic coordinates.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venueinfo" title="class in com.here.sdk.venue.data">`VenueInfo`</a>`>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getVenueInfoList ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  The list of VenueInfo contains venue id and name.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venueinfo" title="class in com.here.sdk.venue.data">`VenueInfo`</a>`>`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getVenueInfoList ( VenueLoadErrorCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  The list of VenueInfo contains venue id and name.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getVenueInfoListAsync ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  The list of VenueInfo contains venue id and name.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getVenueInfoListAsync ( VenueLoadErrorCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  The list of VenueInfo contains venue id and name.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-venue-service-venueservice" title="class in com.here.sdk.venue.service">`VenueService`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getVenueService ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the venue service.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      remove ( VenueDrawingSelectionListener listener)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Removes a drawing selection listener.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      remove ( VenueInfoListListener listener)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Removes a listener for the asynchronous venue info list retrieval.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      remove ( VenueLevelSelectionListener listener)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Removes a level selection listener.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      remove ( VenueLifecycleListener listener)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Removes a venue lifecycle listener.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      remove ( VenueMapLifecycleListener listener)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Removes a venue map lifecycle listener.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      remove ( VenueSelectionListener listener)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Removes a venue selection listener.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      removeVenue ( Venue venue)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Removes a Venue from the VenueMap .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      selectVenueAsync (int venueId)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Downloads a VenueModel if needed and selects a Venue .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      selectVenueAsync (int venueId, VenueLoadErrorCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Downloads a VenueModel if needed and selects a Venue .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      selectVenueAsync ( String venueIdentifier)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Downloads a VenueModel if needed and selects a Venue .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      selectVenueAsync ( String venueIdentifier, VenueLoadErrorCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Downloads a VenueModel if needed and selects a Venue .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setSelectedVenue ( Venue value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the selected Venue .

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

  - <div id="sdk-for-android-navigate-addVenueAsync-int" class="section detail">

    ### addVenueAsync

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addVenueAsync</span><wbr></wbr><span class="parameters">(int venueId)</span>

    </div>

    <div class="block">

    Downloads and adds a Venue to the VenueMap . Method will do nothing if the venue already exists on the venue map.

    </div>

    Parameters:  
    `venueId` -

    The ID of the venue to download and add.

    </div>

  - <div id="sdk-for-android-navigate-addVenueAsync-java-lang-String" class="section detail">

    ### addVenueAsync

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addVenueAsync</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> venueIdentifier)</span>

    </div>

    <div class="block">

    Downloads and adds a Venue to the VenueMap . Method will do nothing if the venue already exists on the venue map.

    </div>

    Parameters:  
    `venueIdentifier` -

    The ID of the venue to download and add.

    </div>

  - <div id="sdk-for-android-navigate-addVenueAsync-int-com-here-sdk-venue-control-VenueLoadErrorCallback" class="section detail">

    ### addVenueAsync

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addVenueAsync</span><wbr></wbr><span class="parameters">(int venueId, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venueloaderrorcallback" title="interface in com.here.sdk.venue.control">VenueLoadErrorCallback</a> callback)</span>

    </div>

    <div class="block">

    Downloads and adds a Venue to the VenueMap . Method will do nothing if the venue already exists on the venue map.

    </div>

    Parameters:  
    `venueId` -

    The ID of the venue to download and add.

    `callback` -

    Callback to receives the error while venue load on the main thread.

    </div>

  - <div id="sdk-for-android-navigate-addVenueAsync-java-lang-String-com-here-sdk-venue-control-VenueLoadErrorCallback" class="section detail">

    ### addVenueAsync

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addVenueAsync</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> venueIdentifier, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venueloaderrorcallback" title="interface in com.here.sdk.venue.control">VenueLoadErrorCallback</a> callback)</span>

    </div>

    <div class="block">

    Downloads and adds a Venue to the VenueMap . Method will do nothing if the venue already exists on the venue map.

    </div>

    Parameters:  
    `venueIdentifier` -

    The ID of the venue to download and add.

    `callback` -

    Callback to receives the error while venue load on the main thread.

    </div>

  - <div id="sdk-for-android-navigate-removeVenue-com-here-sdk-venue-control-Venue" class="section detail">

    ### removeVenue

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeVenue</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control">Venue</a> venue)</span>

    </div>

    <div class="block">

    Removes a Venue from the VenueMap .

    </div>

    Parameters:  
    `venue` -

    The venue to remove.

    </div>

  - <div id="sdk-for-android-navigate-selectVenueAsync-int" class="section detail">

    ### selectVenueAsync

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">selectVenueAsync</span><wbr></wbr><span class="parameters">(int venueId)</span>

    </div>

    <div class="block">

    Downloads a VenueModel if needed and selects a Venue .

    </div>

    Parameters:  
    `venueId` -

    The ID of the venue to download and select.

    </div>

  - <div id="sdk-for-android-navigate-selectVenueAsync-java-lang-String" class="section detail">

    ### selectVenueAsync

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">selectVenueAsync</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> venueIdentifier)</span>

    </div>

    <div class="block">

    Downloads a VenueModel if needed and selects a Venue .

    </div>

    Parameters:  
    `venueIdentifier` -

    The ID of the venue to download and select.

    </div>

  - <div id="sdk-for-android-navigate-selectVenueAsync-int-com-here-sdk-venue-control-VenueLoadErrorCallback" class="section detail">

    ### selectVenueAsync

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">selectVenueAsync</span><wbr></wbr><span class="parameters">(int venueId, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venueloaderrorcallback" title="interface in com.here.sdk.venue.control">VenueLoadErrorCallback</a> callback)</span>

    </div>

    <div class="block">

    Downloads a VenueModel if needed and selects a Venue .

    </div>

    Parameters:  
    `venueId` -

    The ID of the venue to download and select.

    `callback` -

    Callback to receives the error while venue load on the main thread.

    </div>

  - <div id="sdk-for-android-navigate-selectVenueAsync-java-lang-String-com-here-sdk-venue-control-VenueLoadErrorCallback" class="section detail">

    ### selectVenueAsync

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">selectVenueAsync</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> venueIdentifier, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venueloaderrorcallback" title="interface in com.here.sdk.venue.control">VenueLoadErrorCallback</a> callback)</span>

    </div>

    <div class="block">

    Downloads a VenueModel if needed and selects a Venue .

    </div>

    Parameters:  
    `venueIdentifier` -

    The ID of the venue to download and select.

    `callback` -

    Callback to receives the error while venue load on the main thread.

    </div>

  - <div id="sdk-for-android-navigate-cancelVenueSelection" class="section detail">

    ### cancelVenueSelection

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">cancelVenueSelection</span>()

    </div>

    <div class="block">

    Attempts to cancel venue loading and selection that may currently be in progress.

    </div>

    Returns:  
    `True` if a venue was about to load and `false` otherwise.

    </div>

  - <div id="sdk-for-android-navigate-getVenue-com-here-sdk-core-GeoCoordinates" class="section detail">

    ### getVenue

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control">Venue</a></span> <span class="element-name">getVenue</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> position)</span>

    </div>

    <div class="block">

    Tries to find a Venue at the specified geographic coordinates.

    </div>

    Parameters:  
    `position` -

    Geographic coordinates where a venue is located.

    Returns:  
    Venue or `null` if there is no venue at the specified geographic coordinates.

    </div>

  - <div id="sdk-for-android-navigate-getGeometry-com-here-sdk-core-GeoCoordinates" class="section detail">

    ### getGeometry

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a></span> <span class="element-name">getGeometry</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> position)</span>

    </div>

    <div class="block">

    Tries to find a VenueGeometry at the specified geographic coordinates in the selected Venue in the currently selected VenueLevel .

    </div>

    Parameters:  
    `position` -

    Geographic coordinates where the geometry is located.

    Returns:  
    Geometry or `null` if there is no geometry at the specified geographic coordinates.

    </div>

  - <div id="sdk-for-android-navigate-add-com-here-sdk-venue-control-VenueLifecycleListener" class="section detail">

    ### add

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">add</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuelifecyclelistener" title="interface in com.here.sdk.venue.control">VenueLifecycleListener</a> listener)</span>

    </div>

    <div class="block">

    Adds a venue lifecycle listener.

    </div>

    Parameters:  
    `listener` -

    The listener to add.

    </div>

  - <div id="sdk-for-android-navigate-remove-com-here-sdk-venue-control-VenueLifecycleListener" class="section detail">

    ### remove

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">remove</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuelifecyclelistener" title="interface in com.here.sdk.venue.control">VenueLifecycleListener</a> listener)</span>

    </div>

    <div class="block">

    Removes a venue lifecycle listener.

    </div>

    Parameters:  
    `listener` -

    The listener to remove.

    </div>

  - <div id="sdk-for-android-navigate-add-com-here-sdk-venue-control-VenueMapLifecycleListener" class="section detail">

    ### add

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">add</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuemaplifecyclelistener" title="interface in com.here.sdk.venue.control">VenueMapLifecycleListener</a> listener)</span>

    </div>

    <div class="block">

    Adds a venue map lifecycle listener.

    </div>

    Parameters:  
    `listener` -

    The listener to add.

    </div>

  - <div id="sdk-for-android-navigate-remove-com-here-sdk-venue-control-VenueMapLifecycleListener" class="section detail">

    ### remove

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">remove</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuemaplifecyclelistener" title="interface in com.here.sdk.venue.control">VenueMapLifecycleListener</a> listener)</span>

    </div>

    <div class="block">

    Removes a venue map lifecycle listener.

    </div>

    Parameters:  
    `listener` -

    The listener to remove.

    </div>

  - <div id="sdk-for-android-navigate-add-com-here-sdk-venue-control-VenueSelectionListener" class="section detail">

    ### add

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">add</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venueselectionlistener" title="interface in com.here.sdk.venue.control">VenueSelectionListener</a> listener)</span>

    </div>

    <div class="block">

    Adds a venue selection listener.

    </div>

    Parameters:  
    `listener` -

    The listener to add.

    </div>

  - <div id="sdk-for-android-navigate-remove-com-here-sdk-venue-control-VenueSelectionListener" class="section detail">

    ### remove

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">remove</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venueselectionlistener" title="interface in com.here.sdk.venue.control">VenueSelectionListener</a> listener)</span>

    </div>

    <div class="block">

    Removes a venue selection listener.

    </div>

    Parameters:  
    `listener` -

    The listener to remove.

    </div>

  - <div id="sdk-for-android-navigate-add-com-here-sdk-venue-control-VenueDrawingSelectionListener" class="section detail">

    ### add

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">add</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuedrawingselectionlistener" title="interface in com.here.sdk.venue.control">VenueDrawingSelectionListener</a> listener)</span>

    </div>

    <div class="block">

    Adds a drawing selection listener.

    </div>

    Parameters:  
    `listener` -

    The listener to add.

    </div>

  - <div id="sdk-for-android-navigate-remove-com-here-sdk-venue-control-VenueDrawingSelectionListener" class="section detail">

    ### remove

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">remove</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuedrawingselectionlistener" title="interface in com.here.sdk.venue.control">VenueDrawingSelectionListener</a> listener)</span>

    </div>

    <div class="block">

    Removes a drawing selection listener.

    </div>

    Parameters:  
    `listener` -

    The listener to remove.

    </div>

  - <div id="sdk-for-android-navigate-add-com-here-sdk-venue-control-VenueLevelSelectionListener" class="section detail">

    ### add

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">add</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuelevelselectionlistener" title="interface in com.here.sdk.venue.control">VenueLevelSelectionListener</a> listener)</span>

    </div>

    <div class="block">

    Adds a level selection listener.

    </div>

    Parameters:  
    `listener` -

    The listener to add.

    </div>

  - <div id="sdk-for-android-navigate-remove-com-here-sdk-venue-control-VenueLevelSelectionListener" class="section detail">

    ### remove

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">remove</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuelevelselectionlistener" title="interface in com.here.sdk.venue.control">VenueLevelSelectionListener</a> listener)</span>

    </div>

    <div class="block">

    Removes a level selection listener.

    </div>

    Parameters:  
    `listener` -

    The listener to remove.

    </div>

  - <div id="sdk-for-android-navigate-add-com-here-sdk-venue-control-VenueInfoListListener" class="section detail">

    ### add

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">add</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venueinfolistlistener" title="interface in com.here.sdk.venue.control">VenueInfoListListener</a> listener)</span>

    </div>

    <div class="block">

    Adds a listener to handle the completion of the asynchronous venue info list retrieval.

    </div>

    Parameters:  
    `listener` -

    The listener to add.

    </div>

  - <div id="sdk-for-android-navigate-remove-com-here-sdk-venue-control-VenueInfoListListener" class="section detail">

    ### remove

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">remove</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venueinfolistlistener" title="interface in com.here.sdk.venue.control">VenueInfoListListener</a> listener)</span>

    </div>

    <div class="block">

    Removes a listener for the asynchronous venue info list retrieval.

    </div>

    Parameters:  
    `listener` -

    The listener to remove.

    </div>

  - <div id="sdk-for-android-navigate-getVenueInfoList" class="section detail">

    ### getVenueInfoList

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venueinfo" title="class in com.here.sdk.venue.data">VenueInfo</a>\></span> <span class="element-name">getVenueInfoList</span>()

    </div>

    <div class="block">

    The list of VenueInfo contains venue id and name.

    </div>

    Returns:  
    returns the list of object of <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venueinfo" title="class in com.here.sdk.venue.data">`VenueInfo`</a>.

    </div>

  - <div id="sdk-for-android-navigate-getVenueInfoList-com-here-sdk-venue-control-VenueLoadErrorCallback" class="section detail">

    ### getVenueInfoList

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venueinfo" title="class in com.here.sdk.venue.data">VenueInfo</a>\></span> <span class="element-name">getVenueInfoList</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venueloaderrorcallback" title="interface in com.here.sdk.venue.control">VenueLoadErrorCallback</a> callback)</span>

    </div>

    <div class="block">

    The list of VenueInfo contains venue id and name.

    </div>

    Parameters:  
    `callback` -

    Callback to receives the error while venue load on the main thread.

    Returns:  
    returns the list of object of <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venueinfo" title="class in com.here.sdk.venue.data">`VenueInfo`</a>.

    </div>

  - <div id="sdk-for-android-navigate-getVenueInfoListAsync" class="section detail">

    ### getVenueInfoListAsync

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">getVenueInfoListAsync</span>()

    </div>

    <div class="block">

    The list of VenueInfo contains venue id and name. Downloads the list of VenueInfo asynchronously.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-getVenueInfoListAsync-com-here-sdk-venue-control-VenueLoadErrorCallback" class="section detail">

    ### getVenueInfoListAsync

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">getVenueInfoListAsync</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venueloaderrorcallback" title="interface in com.here.sdk.venue.control">VenueLoadErrorCallback</a> callback)</span>

    </div>

    <div class="block">

    The list of VenueInfo contains venue id and name. Downloads the list of VenueInfo asynchronously.

    </div>

    Parameters:  
    `callback` -

    Callback to receive the list of venue info if successful.

    </div>

  - <div id="sdk-for-android-navigate-getTopology-com-here-sdk-core-GeoCoordinates" class="section detail">

    ### getTopology

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuetopology" title="class in com.here.sdk.venue.data">VenueTopology</a></span> <span class="element-name">getTopology</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> position)</span>

    </div>

    <div class="block">

    Tries to find a VenueTopology at the specified geographic coordinates in the selected Venue in the currently selected VenueLevel .

    </div>

    Parameters:  
    `position` -

    Geographic coordinates where the topology is located.

    Returns:  
    Topology or `null` if there is no topology at the specified geographic coordinates.

    </div>

  - <div id="sdk-for-android-navigate-getCrosswalk-com-here-sdk-core-GeoCoordinates" class="section detail">

    ### getCrosswalk

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-data-crosswalk" title="class in com.here.sdk.venue.data">Crosswalk</a></span> <span class="element-name">getCrosswalk</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> position)</span>

    </div>

    <div class="block">

    Tries to find a Crosswalk at the specified geographic coordinates in the selected Venue in the currently selected VenueLevel .

    </div>

    Parameters:  
    `position` -

    Geographic coordinates where the crosswalk is located.

    Returns:  
    Crosswalk or `null` if there is no crosswalk at the specified geographic coordinates.

    </div>

  - <div id="sdk-for-android-navigate-getVenueService" class="section detail">

    ### getVenueService

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-service-venueservice" title="class in com.here.sdk.venue.service">VenueService</a></span> <span class="element-name">getVenueService</span>()

    </div>

    <div class="block">

    Gets the venue service. It can be used to search and get the VenueModel objects.

    </div>

    Returns:  
    The `VenueService` object.

    </div>

  - <div id="sdk-for-android-navigate-getSelectedVenue" class="section detail">

    ### getSelectedVenue

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control">Venue</a></span> <span class="element-name">getSelectedVenue</span>()

    </div>

    <div class="block">

    Gets the currently selected Venue . Use null to deselect the venue.

    </div>

    Returns:  
    The selected venue or `null` if no venue is selected.

    </div>

  - <div id="sdk-for-android-navigate-setSelectedVenue-com-here-sdk-venue-control-Venue" class="section detail">

    ### setSelectedVenue

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSelectedVenue</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control">Venue</a> value)</span>

    </div>

    <div class="block">

    Sets the selected Venue . Use null to deselect the venue.

    </div>

    Parameters:  
    `value` -

    The selected venue or `null` if no venue is selected.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

