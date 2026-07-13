---
title: "tolls property - Section class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-section-tolls"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- tolls.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/Section-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">tolls</span> property

</div>

<div id="sdk-for-flutter-explore-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-routing-toll-class">Toll</a></span>\></span></span> <span class="name">tolls</span>

</div>

<div class="section desc markdown">

All the tolls for this section. Note that tolls are found depending on the transport mode. For example, if pedestrian or bicycle transport mode specified, route sections have no tolls. Indoor route sections have no tolls, too. **Note**: If you're using the `OfflineRoutingEngine`, be aware that this feature is currently in **beta**. As a result, there may be some bugs or unexpected behaviors. Additionally, this feature and related APIs may be updated in future releases without going through the deprecation process. Note that the `OfflineRoutingEngine` is only available with the Navigate license. If you're using the `RoutingEngine`, this feature is considered to be stable. Gets all the tolls for this section. Note that tolls are found depending on the transport mode. For example, if pedestrian or bicycle transport mode specified, route sections have no tolls. Indoor route sections have no tolls, too.

</div>

## Implementation

``` dart
List<Toll> get tolls;
```

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
