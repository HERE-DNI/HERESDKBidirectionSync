---
title: "RoutingConnectionSettings class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-routingconnectionsettings-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RoutingConnectionSettings-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/RoutingConnectionSettings-class-sidebar.html">

<div>

# <span class="kind-class">RoutingConnectionSettings</span> class

</div>

<div class="section desc markdown">

Defines the settings for the retry logic when connecting to the HERE routing backend.

When a timeout is triggered, the next connection attempt starts with a increased timeout. new_timeout = initial_timeout + increment \* retry_count

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-routing-routingconnectionsettings-routingconnectionsettings">RoutingConnectionSettings</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-routing-routingconnectionsettings-connectiontimeoutretryincrease">connectionTimeoutRetryIncrease</a></span> <span class="signature">↔ Duration</span>  
Defines the increase of the timeout for the transfer of data. By default, the initial connection increment per timeout 10 seconds.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-routingconnectionsettings-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-routingconnectionsettings-initialconnectiontimeout">initialConnectionTimeout</a></span> <span class="signature">↔ Duration</span>  
Defines the initial time out for connection to the backend. By default, the initial connection timeout is 5 seconds.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-routingconnectionsettings-initialtransfertimeout">initialTransferTimeout</a></span> <span class="signature">↔ Duration</span>  
Defines the initial time out for data transfer from the backend. By default, the initial transfer timeout is 10 seconds.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-routingconnectionsettings-maxretrycount">maxRetryCount</a></span> <span class="signature">↔ int</span>  
Defines the max amount of retries before the route request failes with connection related error codes. By default, the max amount of retries is 3.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-routingconnectionsettings-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-routingconnectionsettings-transfertimeoutretryincrease">transferTimeoutRetryIncrease</a></span> <span class="signature">↔ Duration</span>  
Defines the increase of the timeout for the connection. By default, the initial transfer increment per timeout is 2 seconds.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-routing-routingconnectionsettings-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-routingconnectionsettings-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-routing-routingconnectionsettings-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
