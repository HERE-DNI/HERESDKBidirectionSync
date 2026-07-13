---
title: "getInstalledRegions method - MapDownloader class - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-mapdownloader-getinstalledregions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getInstalledRegions.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/MapDownloader-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">getInstalledRegions</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-maploader-installedregion-class">InstalledRegion</a></span>\></span></span> <span class="name">getInstalledRegions</span>(<wbr></wbr>)

</div>

<div class="section desc markdown">

Method to get a list of map regions that are currently installed on the device.

Throws if it's not possible to return list of installed regions. Returned list contains:

- successfully downloaded regions, indicated by <a href="sdk-for-flutter-navigate-maploader-installedregionstatus">InstalledRegionStatus.installed</a> in <a href="sdk-for-flutter-navigate-maploader-installedregion-status">InstalledRegion.status</a>;
- regions, that are in the download process, indicated by <a href="sdk-for-flutter-navigate-maploader-installedregionstatus">InstalledRegionStatus.pending</a> in <a href="sdk-for-flutter-navigate-maploader-installedregion-status">InstalledRegion.status</a>;
- regions, which were failed to be downloaded, indicated by <a href="sdk-for-flutter-navigate-maploader-installedregionstatus">InstalledRegionStatus.pending</a> in <a href="sdk-for-flutter-navigate-maploader-installedregion-status">InstalledRegion.status</a>. Note: precise Japan content is stored in separate catalog on the HERE platform, and when corresponding region is downloaded, then the status of siblings and parent regions is set to the <a href="sdk-for-flutter-navigate-maploader-installedregionstatus">InstalledRegionStatus.pending</a> in <a href="sdk-for-flutter-navigate-maploader-installedregion-status">InstalledRegion.status</a>. Precise Japan content is available as an additional offering, please contact sales team for more information.

Returns `List<InstalledRegion>`. List of IDs of regions that are installed on the device

Throws <a href="sdk-for-flutter-navigate-maploader-maploaderexceptionexception-class">MapLoaderExceptionException</a>. Specifies reason, why list of installed regions is not returned.

</div>

## Implementation

``` dart
List<InstalledRegion> getInstalledRegions();
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
