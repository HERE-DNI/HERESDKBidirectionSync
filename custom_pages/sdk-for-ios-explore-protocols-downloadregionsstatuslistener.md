---
title: "DownloadRegionsStatusListener Protocol Reference"
slug: "sdk-for-ios-explore-protocols-downloadregionsstatuslistener"
---

# DownloadRegionsStatusListener

<div class="declaration">

<div class="language">

``` highlight
public protocol DownloadRegionsStatusListener : AnyObject
```

</div>

</div>

Protocol to get notified on status updates when downloading map regions.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk29DownloadRegionsStatusListenerP02onbC8Complete5error7regionsyAA14MapLoaderErrorOSg_SayAA8RegionIdVGSgtF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-onDownloadRegionsComplete-error-regions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-downloadregionsstatuslistener#sdk-for-ios-explore-s-7heresdk29DownloadRegionsStatusListenerP02onbC8Complete5error7regionsyAA14MapLoaderErrorOSg_SayAA8RegionIdVGSgtF" class="token"><code>onDownloadRegionsComplete(error:</code><wbr></wbr><code>regions:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Called after the download for all requested regions has been completed with success or failure. In this callback, failure represents non-retryable error (eg. authentication failure because of invalid credentials and similars). Temporary failures (eg. network errors) are notified through <a href="sdk-for-ios-explore-protocols-downloadregionsstatuslistener#sdk-for-ios-explore-s-7heresdk29DownloadRegionsStatusListenerP7onPause5erroryAA14MapLoaderErrorOSg_tF">`onPause(...)`</a> and downloads will be in paused state so they can be resumed later. Invoked on the main thread.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func onDownloadRegionsComplete(error: MapLoaderError?, regions: [RegionId]?)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-maploadererror">MapLoaderError</a>
  - <a href="sdk-for-ios-explore-structs-regionid">RegionId</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>error</code></em><code> </code></td>
  <td><div>
  <p>Represents an error in case of a failure. It is <code>nil</code> for an operation that succeeds.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>regions</code></em><code> </code></td>
  <td><div>
  <p>Represents a list of regions which has been downloaded. It is <code>nil</code> in case of an error.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk29DownloadRegionsStatusListenerP10onProgress6region10percentageyAA8RegionIdV_s5Int32VtF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-onProgress-region-percentage" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-downloadregionsstatuslistener#sdk-for-ios-explore-s-7heresdk29DownloadRegionsStatusListenerP10onProgress6region10percentageyAA8RegionIdV_s5Int32VtF" class="token"><code>onProgress(region:</code><wbr></wbr><code>percentage:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Called multiple times to indicate the download progress for each requested region individually. Invoked on the main thread.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func onProgress(region: RegionId, percentage: Int32)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-regionid">RegionId</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>region</code></em><code> </code></td>
  <td><div>
  <p>Represents an id of region status update is related to.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>percentage</code></em><code> </code></td>
  <td><div>
  <p>Represents a percentage of data which has been downloaded for particular region.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk29DownloadRegionsStatusListenerP7onPause5erroryAA14MapLoaderErrorOSg_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-onPause-error" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-downloadregionsstatuslistener#sdk-for-ios-explore-s-7heresdk29DownloadRegionsStatusListenerP7onPause5erroryAA14MapLoaderErrorOSg_tF" class="token"><code>onPause(error:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Called when download is paused.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func onPause(error: MapLoaderError?)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-maploadererror">MapLoaderError</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>error</code></em><code> </code></td>
  <td><div>
  <p>Populated when retryable error is a reason of a pause. It is ‘null’ when pause is called by the user.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk29DownloadRegionsStatusListenerP8onResumeyyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-onResume" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-downloadregionsstatuslistener#sdk-for-ios-explore-s-7heresdk29DownloadRegionsStatusListenerP8onResumeyyF" class="token"><code>onResume()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Called when paused download is resumed.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func onResume()
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

