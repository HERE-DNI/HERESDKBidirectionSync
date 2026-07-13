---
title: "VenueLoadErrorCallback typedef - venue.control library - Dart API"
slug: "sdk-for-flutter-navigate-venue.control-venueloaderrorcallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VenueLoadErrorCallback.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="venue.control/venue.control-library-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-typedef">VenueLoadErrorCallback</span> typedef

</div>

<div class="section multi-line-signature">

<span class="name">VenueLoadErrorCallback</span> = <span class="returntype">void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-error" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-control-venueerrorcode">VenueErrorCode</a>?</span> <span class="parameter-name">error</span></span>)</span></span>

</div>

<div class="section desc markdown">

A method which is called on the main thread when <a href="sdk-for-flutter-navigate-venue-control-venuemap-selectvenueasyncwitherrorsstr">VenueMap.selectVenueAsyncWithErrorsStr</a> has been completed.

- `error` Represents an error in case of a failure. It is `null` for an operation that succeeds.

</div>

## Implementation

``` dart
typedef VenueLoadErrorCallback = void Function(VenueErrorCode? error);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
