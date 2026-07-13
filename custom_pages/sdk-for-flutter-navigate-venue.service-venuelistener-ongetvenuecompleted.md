---
title: "onGetVenueCompleted method - VenueListener class - venue.service library - Dart API"
slug: "sdk-for-flutter-navigate-venue.service-venuelistener-ongetvenuecompleted"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onGetVenueCompleted.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="venue.service/VenueListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">onGetVenueCompleted</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">onGetVenueCompleted</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-onGetVenueCompleted-param-venueId" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">venueId</span>, </span>
2.  <span id="sdk-for-flutter-navigate-onGetVenueCompleted-param-venueModel" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-data-venuemodel-class">VenueModel</a>?</span> <span class="parameter-name">venueModel</span>, </span>
3.  <span id="sdk-for-flutter-navigate-onGetVenueCompleted-param-online" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">online</span>, </span>
4.  <span id="sdk-for-flutter-navigate-onGetVenueCompleted-param-venueStyle" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-style-venuestyle-class">VenueStyle</a>?</span> <span class="parameter-name">venueStyle</span>, </span>

)

</div>

<div class="section desc markdown">

Called when loading of a venue or its retrieval from the cache is completed.

- `venueId` The id of the venue.

- `venueModel` The venue model.

- `online` `True` if a new venue was loaded from the server and `false` otherwise.

- `venueStyle` The style associated with the venue.

</div>

## Implementation

``` dart
void onGetVenueCompleted(int venueId, VenueModel? venueModel, bool online, VenueStyle? venueStyle);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
