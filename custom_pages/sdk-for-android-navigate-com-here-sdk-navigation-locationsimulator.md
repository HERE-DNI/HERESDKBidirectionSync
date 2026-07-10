---
title: "LocationSimulator (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-locationsimulator"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.navigation.LocationSimulator → com.here.NativeBase com.here.sdk.navigation.LocationSimulator → com.here.sdk.navigation.LocationSimulator

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">LocationSimulator</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span>

</div>

<div class="block">

Use the LocationSimulator to generate locations along a route or a GPX document. It notifies the registered object about the current location at a fixed interval. In order to customize the interval, see LocationSimulatorOptions . The locations are closely matched to the shape and proceeded from the start to the destination as found in the provided route or the GPX document. When providing a route, the LocationSimulator uses a base speed taken from each span found in the provided route object. This base speed can be multiplied upfront with a custom speedFactor for simulation purposes. Effectively, this means that traffic-related information is not considered to adjust the speed of the simulation. For the GPXTrack , a speed is either based on timestamps in the original file or provided by the user. The following data is read from a GPXTrack and inserted into the provided Location object: latitude , longitude , altitude , time , bearingInDegrees , speedInMetersPerSecond , horizontalAccuracyInMeters , verticalAccuracyInMeters and locationTechnology . Note that simulation works offline and independent from any map data only the information found in the provided route or GPX document is considered. When initializing the LocationSimulator with a route, then interpolations take place between the vertices of the route's polyline. The distance between interpolated locations is a function of the current span's speed and the set notification interval. When initializing the LocationSimulator with a GPX file, the LocationSimulator does not apply any interpolation on the provided location data as this would shadow the recorded GPX data. Notifications will stop after the entire route has been traveled. Note: Map-matched locations are only accessible from RouteProgress .

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

      LocationSimulator ( GPXTrack gpxTrack, LocationSimulatorOptions options)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Create a location simulator

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      LocationSimulator ( Route route, LocationSimulatorOptions options)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance of this class.

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

  <a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener" title="interface in com.here.sdk.core">`LocationListener`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getListener ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets a LocationListener that notifies on location updates.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      pause ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Pauses sending notifications to the subscribers.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      resume ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Resumes sending notifications to the subscribers.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setListener ( LocationListener value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets a LocationListener that notifies on location updates.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      start ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Starts the location provider to send notifications to the subscribers.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      stop ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Stops the location provider from sending notifications to the subscribers.

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

  - <div id="sdk-for-android-navigate-init-com-here-sdk-routing-Route-com-here-sdk-navigation-LocationSimulatorOptions" class="section detail">

    ### LocationSimulator

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">LocationSimulator</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing">Route</a> route, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-locationsimulatoroptions" title="class in com.here.sdk.navigation">LocationSimulatorOptions</a> options)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Creates a new instance of this class.

    </div>

    Parameters:  
    `route` -

    The route to travel.

    `options` -

    The options to specify how the location simulator will behave.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> -

    Indicates what went wrong when the instantiation was attempted.

    </div>

  - <div id="sdk-for-android-navigate-init-com-here-sdk-navigation-GPXTrack-com-here-sdk-navigation-LocationSimulatorOptions" class="section detail">

    ### LocationSimulator

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">LocationSimulator</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxtrack" title="class in com.here.sdk.navigation">GPXTrack</a> gpxTrack, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-locationsimulatoroptions" title="class in com.here.sdk.navigation">LocationSimulatorOptions</a> options)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Create a location simulator

    </div>

    Parameters:  
    `gpxTrack` -

    The GPX track to travel.

    `options` -

    The options to specify how the location simulator will behave.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> -

    Indicates what went wrong when the instantiation was attempted.

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-start" class="section detail">

    ### start

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">start</span>()

    </div>

    <div class="block">

    Starts the location provider to send notifications to the subscribers. Calling this method will always start the location simulator from the route's first Waypoint , even if a simulation has already been started or stopped.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-stop" class="section detail">

    ### stop

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">stop</span>()

    </div>

    <div class="block">

    Stops the location provider from sending notifications to the subscribers.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-pause" class="section detail">

    ### pause

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">pause</span>()

    </div>

    <div class="block">

    Pauses sending notifications to the subscribers. Calling this function has no effect when location provider is not started.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-resume" class="section detail">

    ### resume

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">resume</span>()

    </div>

    <div class="block">

    Resumes sending notifications to the subscribers. Calling this function has no effect when location provider is not started.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-getListener" class="section detail">

    ### getListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener" title="interface in com.here.sdk.core">LocationListener</a></span> <span class="element-name">getListener</span>()

    </div>

    <div class="block">

    Gets a LocationListener that notifies on location updates.

    </div>

    Returns:  
    The object that notifies on location updates.

    </div>

  - <div id="sdk-for-android-navigate-setListener-com-here-sdk-core-LocationListener" class="section detail">

    ### setListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener" title="interface in com.here.sdk.core">LocationListener</a> value)</span>

    </div>

    <div class="block">

    Sets a LocationListener that notifies on location updates.

    </div>

    Parameters:  
    `value` -

    The object that notifies on location updates.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

