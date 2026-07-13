---
title: "startWithToken method - VenueEngine class - venue library - Dart API"
slug: "sdk-for-flutter-navigate-venue-venueengine-startwithtoken"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- startWithToken.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="venue/VenueEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">startWithToken</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">startWithToken</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-startWithToken-param-token" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">token</span></span>

)

</div>

<div class="section desc markdown">

Authenticates asynchronously using HERE SDK credentials using a token to start the <a href="sdk-for-flutter-navigate-venue-service-venueservice-class">VenueService</a>.

An initialization status of the venue service is returned to objects registered as <a href="sdk-for-flutter-navigate-venue-service-venueservicelistener-class">VenueServiceListener</a>. If the authentication will fail, the venue service will not be started.

- `token` SDK project scope token to be used for authentication

</div>

## Implementation

``` dart
void startWithToken(String token);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
