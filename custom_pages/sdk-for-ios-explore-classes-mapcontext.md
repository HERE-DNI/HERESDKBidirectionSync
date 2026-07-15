---
title: "MapContext Class Reference"
slug: "sdk-for-ios-explore-classes-mapcontext"
---

# MapContext

<div class="declaration">

<div class="language">

``` highlight
public class MapContext
```

``` highlight
extension MapContext: NativeBase
```

``` highlight
extension MapContext: Hashable
```

</div>

</div>

MapContext is the rendering engine and the context in which virtual geographic maps get rendered.

It runs the render loop or offers the means for the user to run a custom one.

Data sources, assets and virtual maps can be attached to the context. A virtual map can only render data from sources attached to the same context.

The graphics backend to be used by the engine can be choosen by the user or a platform suitable one can be automatically selected internally. Only one graphics backend can be active and once selected it cannot be changed.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk10MapContextC43SetMemoryManagementOptionsCompletionHandlera"></span>` `<span id="//apple_ref/swift/Alias/SetMemoryManagementOptionsCompletionHandler" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapcontext#/s:7heresdk10MapContextC43SetMemoryManagementOptionsCompletionHandlera" class="token"><code>SetMemoryManagementOptionsCompletionHandler</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Completion handler for the memory management result.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias SetMemoryManagementOptionsCompletionHandler = ( _ result : MapContext . MemoryManagementResult ) -> Void
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
  <td><code> </code><em><code>result</code></em><code> </code></td>
  <td><div>
  <p>The memory management result.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10MapContextC24MemoryManagementStrategyO"></span>` `<span id="//apple_ref/swift/Enum/MemoryManagementStrategy" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapcontext#/s:7heresdk10MapContextC24MemoryManagementStrategyO" class="token"><code>MemoryManagementStrategy</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The memory management strategy. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-classes-mapcontext-memorymanagementstrategy" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum MemoryManagementStrategy : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10MapContextC26MemoryManagementResultCodeO"></span>` `<span id="//apple_ref/swift/Enum/MemoryManagementResultCode" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapcontext#/s:7heresdk10MapContextC26MemoryManagementResultCodeO" class="token"><code>MemoryManagementResultCode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The memory management result code.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-classes-mapcontext-memorymanagementresultcode" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum MemoryManagementResultCode : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10MapContextC12ResourceTypeO"></span>` `<span id="//apple_ref/swift/Enum/ResourceType" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapcontext#/s:7heresdk10MapContextC12ResourceTypeO" class="token"><code>ResourceType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Types of system resources used by <a href="sdk-for-ios-explore-classes-mapcontext">`MapContext`</a> or any of the entities attached to it, like <a href="sdk-for-ios-explore-classes-heremap">`HereMap`</a>.

  <a href="sdk-for-ios-explore-classes-mapcontext-resourcetype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum ResourceType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10MapContextC20FreeResourceSeverityO"></span>` `<span id="//apple_ref/swift/Enum/FreeResourceSeverity" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapcontext#/s:7heresdk10MapContextC20FreeResourceSeverityO" class="token"><code>FreeResourceSeverity</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The severity of a free resource request.

  <a href="sdk-for-ios-explore-classes-mapcontext-freeresourceseverity" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum FreeResourceSeverity : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10MapContextC22MemoryManagementResultV"></span>` `<span id="//apple_ref/swift/Struct/MemoryManagementResult" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapcontext#/s:7heresdk10MapContextC22MemoryManagementResultV" class="token"><code>MemoryManagementResult</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Memory management result.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-classes-mapcontext-memorymanagementresult" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct MemoryManagementResult
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10MapContextC23MemoryManagementOptionsV"></span>` `<span id="//apple_ref/swift/Struct/MemoryManagementOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapcontext#/s:7heresdk10MapContextC23MemoryManagementOptionsV" class="token"><code>MemoryManagementOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Memory management options.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-classes-mapcontext-memorymanagementoptions" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct MemoryManagementOptions
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      freeResource(type: severity: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Frees a system resource held by the `MapContext` and all entities attached to it, like <a href="sdk-for-ios-explore-classes-heremap">`HereMap`</a>. This function is intended for use when a system resource availability becomes low. For example, some memory can be freed when the application transitions to the background state.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func freeResource ( type : MapContext . ResourceType , severity : MapContext . FreeResourceSeverity )
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
  <td><code> </code><em><code>type</code></em><code> </code></td>
  <td><div>
  <p>Type of resource to be freed.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>severity</code></em><code> </code></td>
  <td><div>
  <p>Severity of the request.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      getMemoryManagementOptions()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getMemoryManagementOptions () -> MapContext . MemoryManagementOptions
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  Gets the current memory management options. Returns the actual applied memory limits. If the underlying system limits exceed int32_t max value (2,147,483,647 KiB or ~2 TiB), the returned value is clamped to int32_t max.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  </div>

  </div>

  </div>

- <div>

      setMemoryManagementOptions(_: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets memory management options for controlling tile cache and video memory usage. In <a href="sdk-for-ios-explore-classes-mapcontext-memorymanagementoptions">`MapContext.MemoryManagementOptions`</a> optional parameters with `nil` or non positive values will be ignored, preserving their existing settings.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setMemoryManagementOptions ( _ memoryManagementOptions : MapContext . MemoryManagementOptions , completion : MapContext . SetMemoryManagementOptionsCompletionHandler ?)
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
  <td><code> </code><em><code>memoryManagementOptions</code></em><code> </code></td>
  <td><div>
  <p>The memory management options to set.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Optional handler used upon completion to pass the return value to the caller.</p>
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

<div id="sdk-for-ios-explore-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

