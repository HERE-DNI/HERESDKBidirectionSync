---
title: "MapUpdateVersionCommitPolicy"
slug: "sdk-for-ios-navigate-classes-mapupdater-mapupdateversioncommitpolicy"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/MapUpdateVersionCommitPolicy"></a>
<a title="MapUpdateVersionCommitPolicy Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

<a href="sdk-for-ios-navigate-maploader">MapLoader</a>

<a href="sdk-for-ios-navigate-classes-mapupdater">MapUpdater</a>

        MapUpdateVersionCommitPolicy Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MapUpdateVersionCommitPolicy</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">MapUpdateVersionCommitPolicy</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
<p>Defines if installed regions and subregions are updated one-by-one or if all regions are
updated only once the updates for all installed regions have been downloaded entirely.
This influences the required size of the storage during an update.
Regardless of the set policy, during an update, the previous region data is kept
until the new region data is committed successfully to the persisted storage.
This allows to revert to the previous version in case the update fails.
With <code><a href="../../Classes/MapUpdater/MapUpdateVersionCommitPolicy.html#/s:7heresdk10MapUpdaterC0B25UpdateVersionCommitPolicyO10onCompleteyA2EmF">MapUpdater.MapUpdateVersionCommitPolicy.onComplete</a></code>, more data has to be kept until
the update process finishes, while <code><a href="../../Classes/MapUpdater/MapUpdateVersionCommitPolicy.html#/s:7heresdk10MapUpdaterC0B25UpdateVersionCommitPolicyO13onFirstRegionyA2EmF">MapUpdater.MapUpdateVersionCommitPolicy.onFirstRegion</a></code>
allows to make faster use of the downloaded region and requires less disk space as only the
currently updated region is kept until the process completes.
However, with an <code><a href="../../Classes/MapUpdater/MapUpdateVersionCommitPolicy.html#/s:7heresdk10MapUpdaterC0B25UpdateVersionCommitPolicyO13onFirstRegionyA2EmF">MapUpdater.MapUpdateVersionCommitPolicy.onFirstRegion</a></code> policy the overall
process can be less reliable and bears a higher risk of errors.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapUpdaterC0B25UpdateVersionCommitPolicyO13onFirstRegionyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/onFirstRegion"></a>
<a class="token" href="#/s:7heresdk10MapUpdaterC0B25UpdateVersionCommitPolicyO13onFirstRegionyA2EmF">onFirstRegion</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Updates the cache and the persisted storage once the first region was fully downloaded.
If only one region was requested, this setting is equivalent to <code><a href="../../Classes/MapUpdater/MapUpdateVersionCommitPolicy.html#/s:7heresdk10MapUpdaterC0B25UpdateVersionCommitPolicyO10onCompleteyA2EmF">MapUpdater.MapUpdateVersionCommitPolicy.onComplete</a></code>.
If more regions or subregions are requested, then the policy will apply.
For example, if Germany is requested to be updated, then the cache and the persisted
storage will be updated as soon as any contained subregion such as Berlin or Brandenburg
has been fully downloaded. The previous data for a region will be removed once
that specific region has been updated successfully.
However, the <code><a href="sdk-for-ios-navigate-classes-mapversionhandle">MapVersionHandle</a></code> will be updated once the first region has
been installed. This inconsistency will be gone, once the update process completes.
In case of errors, or an aborted update process, <code><a href="../../MapLoader.html#/s:7heresdk26CatalogsUpdateInfoCallbacka">CatalogsUpdateInfoCallback</a></code>
indicates that still an update is available until the process was successfully repeated.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">onFirstRegion</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapUpdaterC0B25UpdateVersionCommitPolicyO10onCompleteyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/onComplete"></a>
<a class="token" href="#/s:7heresdk10MapUpdaterC0B25UpdateVersionCommitPolicyO10onCompleteyA2EmF">onComplete</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Commits the new map version to the cache and the persisted storage once all previously
installed regions have been updated. For example, if Germany needs an update, then
all previous data is kept until Germany including all subregions has been downloaded.
This update process is more reliable than <code><a href="../../Classes/MapUpdater/MapUpdateVersionCommitPolicy.html#/s:7heresdk10MapUpdaterC0B25UpdateVersionCommitPolicyO13onFirstRegionyA2EmF">MapUpdater.MapUpdateVersionCommitPolicy.onFirstRegion</a></code>,
but requires more free storage space until the process completes. Besides, users need to wait longer until
they can use all updated regions.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">onComplete</span></code></pre>
</div>
</div>
</section>
</div>
</li>
</ul>
</div>
</section>
</section>
<section id="footer">
<p>© 2026 <a class="link" href="" rel="external noopener" target="_blank"></a>. All rights reserved. (Last updated: 2026-04-14)</p>
<p>Generated by <a class="link" href="https://github.com/realm/jazzy" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a class="link" href="https://realm.io" rel="external noopener" target="_blank">Realm</a> project.</p>
</section>
</article>
</div>
</body>
</html>

`
} </HTMLBlock>
