import json,onnx
d=json.load(open('fa_IR-mana-medium.onnx.json'))
with open('tokens.txt','w',encoding='utf-8') as f:
  for s,ids in d['phoneme_id_map'].items():
    for i in ids: f.write(f"{s} {i}\n")
m=onnx.load('fa_IR-mana-medium.onnx')
meta={"model_type":"vits","comment":"piper","language":"Persian","voice":"fa","has_espeak":1,"n_speakers":1,"sample_rate":d['audio']['sample_rate']}
del m.metadata_props[:]
for k,v in meta.items():
  p=m.metadata_props.add();p.key=k;p.value=str(v)
onnx.save(m,'model.onnx')
