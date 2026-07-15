---
title: "EVSearchEngine Class Reference"
slug: "sdk-for-ios-navigate-classes-evsearchengine"
---

# EVSearchEngine

<div class="declaration">

<div class="language">

``` highlight
public class EVSearchEngine : EVSearchInterface
```

``` highlight
extension EVSearchEngine: NativeBase
```

``` highlight
extension EVSearchEngine: Hashable
```

</div>

</div>

The `EVSearchEngine` API provides detailed information about charging locations. It requires an online connection to execute the requests. A licence is required to use this API. Details can be found in <a href="https://www.here.com/docs/bundle/ev-charge-points-api-v3-developer-guide/page/topics/quick-start-platform.html">HERE EV Charge Points API v3 - Developer Guide</a>.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

      init()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of this class.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-core#/s:7heresdk18InstantiationErrora">`InstantiationError`</a> Indicates what went wrong when the instantiation was attempted.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init () throws
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      init(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of this class.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-core#/s:7heresdk18InstantiationErrora">`InstantiationError`</a> Indicates what went wrong when the instantiation was attempted.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( _ sdkEngine : SDKNativeEngine ) throws
  ```

  </pre>

  </div>

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
  <td><code> </code><em><code>sdkEngine</code></em><code> </code></td>
  <td><div>
  <p>Instance of an existing SDKEngine.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      search(ids: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Performs an asynchronous request for <a href="sdk-for-ios-navigate-classes-evcharginglocation">`EVChargingLocation`</a> instances with given Place IDs.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult public func search ( ids : [ String ], completion : @escaping EVCP3SearchCompletionHandler ) -> TaskHandle
  ```

  </pre>

  </div>

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
  <td><code> </code><em><code>ids</code></em><code> </code></td>
  <td><div>
  <p>List of charging location identifiers.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback which receives the result on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

  </div>

  </div>

  </div>

- <div>

      setOptions(options: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Configures the behavior of `EVSearchEngine` using the provided input options.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setOptions ( options : EVSearchOptions )
  ```

  </pre>

  </div>

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
  <td><code> </code><em><code>options</code></em><code> </code></td>
  <td><div>
  <p>Options used to customize how <code>EVSearchEngine</code> behaves.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-navigate-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

