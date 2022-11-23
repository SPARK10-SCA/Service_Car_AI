import matplotlib.pyplot as plt
import json

f = open('../../data/result_log/[damage]test_evaluation_log.json')
data = json.load(f)

name = data['start_at_kst']
train_loss = []
val_loss = []

for i in data['train_log']:
    train_loss.append(i['train_loss'])
    val_loss.append(i['eval']['summary']['average Loss'])

train_loss = [val for sublist in train_loss for val in sublist]

f.close()

# plot the training loss
plt.style.use("ggplot")
plt.figure()
plt.plot(train_loss, label="train_loss")
plt.plot(val_loss, label="val_loss")
plt.title("Training Loss on Dataset")
plt.xlabel("Epoch #")
plt.ylabel("Loss")
plt.legend(loc="upper right")
plt.savefig('../../data/result_log/loss_'+name)

plt.show()