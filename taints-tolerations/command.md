Taint a node with 

```
kubectl taint node minikube node-type=production:NoSchedule
```

- key: node-type
- value: production (optional)
- effect: NoSchedule
