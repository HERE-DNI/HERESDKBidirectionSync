---
title: "MapUpdateVersionCommitPolicy Enumeration Reference"
slug: "sdk-for-ios-explore-classes-mapupdater-mapupdateversioncommitpolicy"
---

# MapUpdateVersionCommitPolicy

<div class="declaration">

<div class="language">

``` highlight
public enum MapUpdateVersionCommitPolicy : UInt32, CaseIterable, Codable
```

</div>

</div>

Defines if installed regions and subregions are updated one-by-one or if all regions are updated only once the updates for all installed regions have been downloaded entirely. This influences the required size of the storage during an update. Regardless of the set policy, during an update, the previous region data is kept until the new region data is committed successfully to the persisted storage. This allows to revert to the previous version in case the update fails. With <a href="sdk-for-ios-explore-classes-mapupdater-mapupdateversioncommitpolicy#/s:7heresdk10MapUpdaterC0B25UpdateVersionCommitPolicyO10onCompleteyA2EmF">`MapUpdater.MapUpdateVersionCommitPolicy.onComplete`</a>, more data has to be kept until the update process finishes, while <a href="sdk-for-ios-explore-classes-mapupdater-mapupdateversioncommitpolicy#/s:7heresdk10MapUpdaterC0B25UpdateVersionCommitPolicyO13onFirstRegionyA2EmF">`MapUpdater.MapUpdateVersionCommitPolicy.onFirstRegion`</a> allows to make faster use of the downloaded region and requires less disk space as only the currently updated region is kept until the process completes. However, with an <a href="sdk-for-ios-explore-classes-mapupdater-mapupdateversioncommitpolicy#/s:7heresdk10MapUpdaterC0B25UpdateVersionCommitPolicyO13onFirstRegionyA2EmF">`MapUpdater.MapUpdateVersionCommitPolicy.onFirstRegion`</a> policy the overall process can be less reliable and bears a higher risk of errors.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk10MapUpdaterC0B25UpdateVersionCommitPolicyO13onFirstRegionyA2EmF"></span>` `<span id="//apple_ref/swift/Element/onFirstRegion" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapupdater-mapupdateversioncommitpolicy#/s:7heresdk10MapUpdaterC0B25UpdateVersionCommitPolicyO13onFirstRegionyA2EmF" class="token"><code>onFirstRegion</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Updates the cache and the persisted storage once the first region was fully downloaded. If only one region was requested, this setting is equivalent to <a href="sdk-for-ios-explore-classes-mapupdater-mapupdateversioncommitpolicy#/s:7heresdk10MapUpdaterC0B25UpdateVersionCommitPolicyO10onCompleteyA2EmF">`MapUpdater.MapUpdateVersionCommitPolicy.onComplete`</a>. If more regions or subregions are requested, then the policy will apply. For example, if Germany is requested to be updated, then the cache and the persisted storage will be updated as soon as any contained subregion such as Berlin or Brandenburg has been fully downloaded. The previous data for a region will be removed once that specific region has been updated successfully. However, the <a href="sdk-for-ios-explore-classes-mapversionhandle">`MapVersionHandle`</a> will be updated once the first region has been installed. This inconsistency will be gone, once the update process completes. In case of errors, or an aborted update process, <a href="sdk-for-ios-explore-maploader#/s:7heresdk26CatalogsUpdateInfoCallbacka">`CatalogsUpdateInfoCallback`</a> indicates that still an update is available until the process was successfully repeated.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case onFirstRegion
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10MapUpdaterC0B25UpdateVersionCommitPolicyO10onCompleteyA2EmF"></span>` `<span id="//apple_ref/swift/Element/onComplete" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapupdater-mapupdateversioncommitpolicy#/s:7heresdk10MapUpdaterC0B25UpdateVersionCommitPolicyO10onCompleteyA2EmF" class="token"><code>onComplete</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Commits the new map version to the cache and the persisted storage once all previously installed regions have been updated. For example, if Germany needs an update, then all previous data is kept until Germany including all subregions has been downloaded. This update process is more reliable than <a href="sdk-for-ios-explore-classes-mapupdater-mapupdateversioncommitpolicy#/s:7heresdk10MapUpdaterC0B25UpdateVersionCommitPolicyO13onFirstRegionyA2EmF">`MapUpdater.MapUpdateVersionCommitPolicy.onFirstRegion`</a>, but requires more free storage space until the process completes. Besides, users need to wait longer until they can use all updated regions.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case onComplete
  ```

  </div>

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-explore-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

