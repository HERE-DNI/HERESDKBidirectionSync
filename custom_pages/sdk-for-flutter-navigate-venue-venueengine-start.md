---
title: "start method - VenueEngine class - venue library - Dart API"
slug: "sdk-for-flutter-navigate-venue-venueengine-start"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- start.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="venue/VenueEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">start</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">start</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-start-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-authenticationcallback">AuthenticationCallback</a>?</span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Authenticates asynchronously using HERE SDK credentials and uses a result token to start the <a href="sdk-for-flutter-navigate-venue-service-venueservice-class">VenueService</a>.

An initialization status of the venue service is returned to objects registered as <a href="sdk-for-flutter-navigate-venue-service-venueservicelistener-class">VenueServiceListener</a>. If the authentication will fail, the venue service will not be started.

- `callback` The optional callback that will be triggered when the authentication will be completed. If the authentication fails, the venue service will not be started.

</div>

## Implementation

``` dart
void start(AuthenticationCallback? callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
