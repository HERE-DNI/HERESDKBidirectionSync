---
title: "startRendering method - VisualNavigator class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-visualnavigator-startrendering"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/VisualNavigator-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">startRendering</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">startRendering</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-startRendering-param-mapView" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-class">MapViewBase</a></span> <span class="parameter-name">mapView</span></span>

)

</div>

<div class="section desc markdown">

Starts visual navigation rendering.

A preconfigured current location marker is shown as soon as a location is received. The marker is chosen according to the transport mode specified in the route. If no route is present, the marker is chosen based on the <a href="sdk-for-flutter-navigate-navigation-navigatorinterface-trackingtransportspecification">NavigatorInterface.trackingTransportSpecification</a> property. Calling startRendering() changes the <a href="sdk-for-flutter-navigate-mapview-mapcamera-principalpoint">MapCamera.principalPoint</a> property so that the current position indicator is equal to the value from <a href="sdk-for-flutter-navigate-navigation-camerabehavior-normalizedprincipalpoint">CameraBehavior.normalizedPrincipalPoint</a>, in which by default places the principal point slightly at the bottom of the mapview. It is restored to its original value when stopRendering() is called. **Note:** When rendering is started again for a new map view instance, rendering is automatically stopped on the previous map view instance. Also note that the <a href="sdk-for-flutter-navigate-mapview-mapviewbase-framerate">MapViewBase.frameRate</a> can be lowered to reduce CPU usage, to adjust for tradeoffs between rendering smoothness versus battery consumption.

- `mapView` The map view on which visual navigation will take place.

</div>

## Implementation

``` dart
void startRendering(MapViewBase mapView);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

