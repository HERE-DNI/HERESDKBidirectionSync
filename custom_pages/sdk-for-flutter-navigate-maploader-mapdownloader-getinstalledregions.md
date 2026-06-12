---
title: "getInstalledRegions abstract method"
slug: "sdk-for-flutter-navigate-maploader-mapdownloader-getinstalledregions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getInstalledRegions.html -->


<div>
<h1>getInstalledRegions abstract method</h1></div>

List&lt;<a href="/sdk-for-flutter-navigate-maploader-installedregion-class">InstalledRegion</a>&gt;
getInstalledRegions()

      

    

<p>Method to get a list of map regions that are currently installed on the device.</p>
<p>Throws if it's not possible to return list of installed regions.
Returned list contains:</p>
<ul>
<li>successfully downloaded regions, indicated by <a href="/sdk-for-flutter-navigate-maploader-installedregionstatus">InstalledRegionStatus.installed</a> in <a href="/sdk-for-flutter-navigate-maploader-installedregion-status">InstalledRegion.status</a>;</li>
<li>regions, that are in the download process, indicated by <a href="/sdk-for-flutter-navigate-maploader-installedregionstatus">InstalledRegionStatus.pending</a> in <a href="/sdk-for-flutter-navigate-maploader-installedregion-status">InstalledRegion.status</a>;</li>
<li>regions, which were failed to be downloaded, indicated by <a href="/sdk-for-flutter-navigate-maploader-installedregionstatus">InstalledRegionStatus.pending</a> in <a href="/sdk-for-flutter-navigate-maploader-installedregion-status">InstalledRegion.status</a>.
Note: precise Japan content is stored in separate catalog on the HERE platform, and when corresponding region is downloaded, then the status of siblings and parent regions is
set to the <a href="/sdk-for-flutter-navigate-maploader-installedregionstatus">InstalledRegionStatus.pending</a> in <a href="/sdk-for-flutter-navigate-maploader-installedregion-status">InstalledRegion.status</a>. Precise Japan content is available as an additional offering, please contact sales team for more information.</li>
</ul>
<p>Returns <code>List&lt;InstalledRegion&gt;</code>. List of IDs of regions that are installed on the device</p>
<p>Throws <a href="/sdk-for-flutter-navigate-maploader-maploaderexceptionexception-class">MapLoaderExceptionException</a>. Specifies reason, why list of installed regions is not returned.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;InstalledRegion&gt; getInstalledRegions();</code></pre>

 



</div>
`
}</HTMLBlock>
