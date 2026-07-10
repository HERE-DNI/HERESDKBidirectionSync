---
title: "GPXTrackWriter (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-gpxtrackwriter"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.navigation.GPXTrackWriter → com.here.NativeBase com.here.sdk.navigation.GPXTrackWriter → com.here.sdk.navigation.GPXTrackWriter

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

All Implemented Interfaces:  
<a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener" title="interface in com.here.sdk.core">`LocationListener`</a>

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">GPXTrackWriter</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a> implements <a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener" title="interface in com.here.sdk.core">LocationListener</a></span>

</div>

<div class="block">

Writes GPX track points to GPXTrack . The instance of the class should be added as a listener to the LocationEngine for GPX track recording. Appends the new location to the back segment of the track whenever the listener is called. The following data (if provided) can be recorded and inserted into the resulting GPXTrack : latitude , longitude , altitude , time , bearingInDegrees , pitchInDegrees , speedInMetersPerSecond , horizontalAccuracyInMeters , verticalAccuracyInMeters , bearingAccuracyInDegrees , speedAccuracyInMetersPerSecond and locationTechnology . Use case examples: A user wants to create and save a new GPXDocument with one GPXTrack : - create GPXTrackWriter and add it as a location listener to LocationEngine . - set user parameters to getTrack() (e.g. GPXTrack.getName() or GPXTrack.getDescription() ). - when writing is completed, create a new GPXDocument with a list of one GPXTrack and save the document via GPXDocument.save(java.lang.String) . A user wants to modify and save GPXTrack in the existing GPXDocument : - load GPXDocument from a file by the relevant constructor. - create GPXTrackWriter with the required track in the list GPXDocument.getTracks() , add the created instance as a location listener to LocationEngine . - when writing is completed, save the document via GPXDocument.save(java.lang.String) . The GPXDocument including all tracks is saved in the GPX file format. Hence, once saved, it can be easily shared with other applications that understand the GPX file format.

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

      GPXTrackWriter ()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance of GPXTrackWriter with an empty track inside.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      GPXTrackWriter ( GPXTrack track)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance of GPXTrackWriter with GPXTrack .

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

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxtrack" title="class in com.here.sdk.navigation">`GPXTrack`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTrack ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the GPX track into which GPX track points are written.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      onLocationUpdated ( Location location)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Called each time a new location is available.

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

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init" class="section detail">

    ### GPXTrackWriter

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">GPXTrackWriter</span>()

    </div>

    <div class="block">

    Creates a new instance of GPXTrackWriter with an empty track inside.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-init-com-here-sdk-navigation-GPXTrack" class="section detail">

    ### GPXTrackWriter

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">GPXTrackWriter</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxtrack" title="class in com.here.sdk.navigation">GPXTrack</a> track)</span>

    </div>

    <div class="block">

    Creates a new instance of GPXTrackWriter with GPXTrack . Use this constructor to append locations to an existing track.

    </div>

    Parameters:  
    `track` -

    GPX track.

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-getTrack" class="section detail">

    ### getTrack

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxtrack" title="class in com.here.sdk.navigation">GPXTrack</a></span> <span class="element-name">getTrack</span>()

    </div>

    <div class="block">

    Gets the GPX track into which GPX track points are written.

    </div>

    Returns:  
    GPX track into which GPX track points are written.

    </div>

  - <div id="sdk-for-android-navigate-onLocationUpdated-com-here-sdk-core-Location" class="section detail">

    ### onLocationUpdated

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">onLocationUpdated</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-location" title="class in com.here.sdk.core">Location</a> location)</span>

    </div>

    <div class="block">

    Called each time a new location is available. In a navigation context while using the Navigator or VisualNavigator , it's required to set the Location.time parameter for each Location object so that the HERE SDK can map-match the locations properly. If the Location.time parameter is missing, the location will be ignored. For navigation, it is also recommended to provide the bearing and speed parameters for each Location object. Invoked on the main thread.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener#onLocationUpdated(com.here.sdk.core.Location">`onLocationUpdated`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener" title="interface in com.here.sdk.core">`LocationListener`</a>

    Parameters:  
    `location` -

    Current location.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

