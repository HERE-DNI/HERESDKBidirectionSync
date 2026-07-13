---
title: "addListener method - RasterDataSource class - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-explore-mapview.datasource-rasterdatasource-addlistener"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/RasterDataSource-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">addListener</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">addListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-addListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-rasterdatasourcelistener-class">RasterDataSourceListener</a></span> <span class="parameter-name">listener</span></span>

)

</div>

<div class="section desc markdown">

Add listener for receiving state notifications.

The new listener is appended to the set of data source listeners as a strong reference and will receive only the notifications occurring after the registration. Caller is responsible for releasing the strong reference by calling <a href="sdk-for-flutter-explore-mapview-datasource-rasterdatasource-removelistener">RasterDataSource.removeListener</a>. The state notifications can occur on an arbitrary thread.

- `listener` Listener to be added for receiving state notifications.

</div>

## Implementation

``` dart
void addListener(RasterDataSourceListener listener);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

