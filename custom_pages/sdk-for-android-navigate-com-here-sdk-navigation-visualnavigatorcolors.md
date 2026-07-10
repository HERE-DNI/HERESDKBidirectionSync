---
title: "VisualNavigatorColors (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-visualnavigatorcolors"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.navigation.VisualNavigatorColors → com.here.NativeBase com.here.sdk.navigation.VisualNavigatorColors → com.here.sdk.navigation.VisualNavigatorColors

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">VisualNavigatorColors</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span>

</div>

<div class="block">

This class contains colors used by VisualNavigator to render the route and the maneuver arrow visualization.

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="sdk-for-android-navigate-com-here-sdk-navigation-visualnavigatorcolors" title="class in com.here.sdk.navigation">`VisualNavigatorColors`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      dayColors ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Retrieves HERE day color presets for route and maneuver arrow visualization.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">`Color`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getManeuverArrowColor ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the color used to draw maneuver arrows on the route.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-routeprogresscolors" title="class in com.here.sdk.navigation">`RouteProgressColors`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getRouteProgressColors ( SectionTransportMode sectionTransportMode)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets route color for visualization.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficonroutecolors" title="class in com.here.sdk.navigation">`TrafficOnRouteColors`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTrafficOnRouteColors ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets colors used for visualization of traffic conditions on route.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="sdk-for-android-navigate-com-here-sdk-navigation-visualnavigatorcolors" title="class in com.here.sdk.navigation">`VisualNavigatorColors`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      nightColors ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Retrieves HERE night color presets for route and maneuver arrow visualization.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setManeuverArrowColor ( Color value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the color used to draw maneuver arrows on the route.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setRouteProgressColors ( SectionTransportMode sectionTransportMode, RouteProgressColors routeProgressColors)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets route color for visualization.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setTrafficOnRouteColors ( TrafficOnRouteColors value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets colors used for visualization of traffic conditions on route.

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

  - <div id="sdk-for-android-navigate-setRouteProgressColors-com-here-sdk-routing-SectionTransportMode-com-here-sdk-navigation-RouteProgressColors" class="section detail">

    ### setRouteProgressColors

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRouteProgressColors</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-sectiontransportmode" title="enum class in com.here.sdk.routing">SectionTransportMode</a> sectionTransportMode, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-routeprogresscolors" title="class in com.here.sdk.navigation">RouteProgressColors</a> routeProgressColors)</span>

    </div>

    <div class="block">

    Sets route color for visualization.

    </div>

    Parameters:  
    `sectionTransportMode` -

    The section transport mode.

    `routeProgressColors` -

    The route progress colors.

    </div>

  - <div id="sdk-for-android-navigate-getRouteProgressColors-com-here-sdk-routing-SectionTransportMode" class="section detail">

    ### getRouteProgressColors

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-routeprogresscolors" title="class in com.here.sdk.navigation">RouteProgressColors</a></span> <span class="element-name">getRouteProgressColors</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-sectiontransportmode" title="enum class in com.here.sdk.routing">SectionTransportMode</a> sectionTransportMode)</span>

    </div>

    <div class="block">

    Gets route color for visualization.

    </div>

    Parameters:  
    `sectionTransportMode` -

    The section transport mode.

    Returns:  
    The route color for visualization.

    </div>

  - <div id="sdk-for-android-navigate-dayColors" class="section detail">

    ### dayColors

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-visualnavigatorcolors" title="class in com.here.sdk.navigation">VisualNavigatorColors</a></span> <span class="element-name">dayColors</span>()

    </div>

    <div class="block">

    Retrieves HERE day color presets for route and maneuver arrow visualization.

    </div>

    Returns:  
    HERE day color presets for route and maneuver arrow visualization.

    </div>

  - <div id="sdk-for-android-navigate-nightColors" class="section detail">

    ### nightColors

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-visualnavigatorcolors" title="class in com.here.sdk.navigation">VisualNavigatorColors</a></span> <span class="element-name">nightColors</span>()

    </div>

    <div class="block">

    Retrieves HERE night color presets for route and maneuver arrow visualization.

    </div>

    Returns:  
    HERE night color presets for route and maneuver arrow visualization.

    </div>

  - <div id="sdk-for-android-navigate-getManeuverArrowColor" class="section detail">

    ### getManeuverArrowColor

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a></span> <span class="element-name">getManeuverArrowColor</span>()

    </div>

    <div class="block">

    Gets the color used to draw maneuver arrows on the route. The object containing color used to draw maneuver arrows on the route to highlight lane directions at the end of a street. The alpha channel is ignored. The color is interpreted as fully opaque.

    </div>

    Returns:  
    Maneuver arrow color.

    </div>

  - <div id="sdk-for-android-navigate-setManeuverArrowColor-com-here-sdk-core-Color" class="section detail">

    ### setManeuverArrowColor

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setManeuverArrowColor</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> value)</span>

    </div>

    <div class="block">

    Sets the color used to draw maneuver arrows on the route. The alpha channel is ignored. The object containing color used to draw maneuver arrows on the route to highlight lane directions at the end of a street. The alpha channel is ignored. The color is interpreted as fully opaque.

    </div>

    Parameters:  
    `value` -

    Maneuver arrow color.

    </div>

  - <div id="sdk-for-android-navigate-getTrafficOnRouteColors" class="section detail">

    ### getTrafficOnRouteColors

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficonroutecolors" title="class in com.here.sdk.navigation">TrafficOnRouteColors</a></span> <span class="element-name">getTrafficOnRouteColors</span>()

    </div>

    <div class="block">

    Gets colors used for visualization of traffic conditions on route.

    </div>

    Returns:  
    Colors used to visualize traffic conditions on the route ahead of the current location, for segments with a jam factor of 4.0 or higher. For route segments with a jam factor below 4.0 and those behind the current location, <a href="sdk-for-android-navigate-com-here-sdk-navigation-routeprogresscolors" title="class in com.here.sdk.navigation">`RouteProgressColors`</a> are used instead.

    </div>

  - <div id="sdk-for-android-navigate-setTrafficOnRouteColors-com-here-sdk-navigation-TrafficOnRouteColors" class="section detail">

    ### setTrafficOnRouteColors

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTrafficOnRouteColors</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficonroutecolors" title="class in com.here.sdk.navigation">TrafficOnRouteColors</a> value)</span>

    </div>

    <div class="block">

    Sets colors used for visualization of traffic conditions on route.

    </div>

    Parameters:  
    `value` -

    Colors used to visualize traffic conditions on the route ahead of the current location, for segments with a jam factor of 4.0 or higher. For route segments with a jam factor below 4.0 and those behind the current location, <a href="sdk-for-android-navigate-com-here-sdk-navigation-routeprogresscolors" title="class in com.here.sdk.navigation">`RouteProgressColors`</a> are used instead.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

